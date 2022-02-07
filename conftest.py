import jsondiff
import pytest
import psycopg2
import pprint

from django.db import connections
from django.conf import settings
from django.core import management
from django.test import Client
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


ddl_connection = dict(
        host=settings.DATABASES['ddl']['HOST'],
        port=settings.DATABASES['ddl']['PORT'],
        database=settings.DATABASES['ddl']['NAME'],
        user=settings.DATABASES['ddl']['USER'],
        password=settings.DATABASES['ddl']['PASSWORD']
    )


def run_sql(sql):
    try:
        conn = psycopg2.connect(**ddl_connection)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(sql)
    finally:
        if conn:
            conn.close()


def manage(*args):
    management.execute_from_command_line(['manage', *args])


@pytest.fixture(autouse=True)
def set_test_database(settings):
    settings.DATABASES['default'] = settings.DATABASES['test']


@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_blocker):
    database = settings.DATABASES['test']['NAME']
    user = settings.DATABASES['test']['USER']
    password = settings.DATABASES['test']['PASSWORD']

    run_sql(
        f"""
        SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = '{database}'
          AND pid <> pg_backend_pid();
        """
    )
    try:
        run_sql(f"CREATE USER {user} WITH PASSWORD '{password}'")
    except:
        run_sql(f"ALTER USER {user} WITH PASSWORD '{password}'")

    run_sql(f"DROP DATABASE IF EXISTS {database}")
    run_sql(f"CREATE DATABASE {database} OWNER {user}")
    run_sql(f"GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO {user}")
    run_sql(f"ALTER ROLE {user} SUPERUSER")
    run_sql(f"CREATE EXTENSION IF NOT EXISTS citext")

    with django_db_blocker.unblock():
        manage('migrate')

    yield
    for connection in connections.all():
        connection.close()
    run_sql(f"DROP DATABASE {database}")


@pytest.fixture
def login_user(db):
    # `db` fixture needs to avoid error "Database access not allowed"
    # if database is not used

    def inner(username, password):
        client = Client()
        if client.login(username=username, password=password):
            return client
        else:
            raise ValueError('Login fail {username} {password}')
    return inner


@pytest.fixture
def admin(login_user):
    return login_user(username='admin', password='P@ssw0rd')


def pformat(data):
    return pprint.pformat(data, indent=2, width=120)


@pytest.fixture
def make_diff():
    def wrapper(expected, actual, ignore=(), skip_unexpected=False):

        def edit_actual(origin, expected):
            res = {k: v for k, v in origin.items() if k not in ignore}
            if skip_unexpected:
                res = {k: v for k, v in res.items() if k in expected}
            return res

        is_dict = lambda x: isinstance(x, dict)
        is_list = lambda x: isinstance(x, list)
        if all(map(is_dict, [actual, expected])):
            actual_edited = edit_actual(actual, expected.keys())
            expected_edited = {k: v for k, v in expected.items() if k not in ignore}

        elif all(map(is_list, [actual, expected])) and all(map(lambda x: all(map(
                is_dict, x)), [expected, actual])):
            expected_edited = []
            expected_keys = set()
            for x in expected:
                expected_edited.append({k: v for k, v in x.items() if k not in ignore})
                expected_keys.update(x.keys())

            actual_edited = [edit_actual(x, expected_keys) for x in actual]

        diff = jsondiff.diff(expected_edited, actual_edited, syntax='symmetric',
                             marshal=True)
        return (
            '\n$EXPECTED: \n{}\n\n$ACTUAL: \n{}\n\n$DIFF: \n{}\n'.format(
                pformat(expected), pformat(actual), pformat(diff)
            )
            if diff
            else ''
        )
    return wrapper
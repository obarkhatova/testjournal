import pytest
import psycopg2

from django.db import connections
from django.conf import settings
from django.core import management
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

    with django_db_blocker.unblock():
        manage('migrate')

    yield
    for connection in connections.all():
        connection.close()
    run_sql(f"DROP DATABASE {database}")

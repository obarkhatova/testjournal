from django.db import migrations
from django.contrib.auth import get_user_model


def create_admin(apps, schema_editor):
    User = get_user_model()
    u = User(
        username='admin',
        firstname='Sam',
        lastname='Brosnan',
        email='1@mail.com',
        is_staff=True,
        is_superuser=True,
        is_active=True,
    )
    u.set_password('P@ssw0rd')
    u.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_user'),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]

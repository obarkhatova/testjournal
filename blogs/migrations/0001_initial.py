from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                primary_key=True,
                                                related_name='blog',
                                                serialize=False,
                                                to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

import choicesenum.django.fields
from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0002_blog_instance_auto_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('published', models.DateField(null=True)),
                ('content', models.TextField()),
                ('status', choicesenum.django.fields.EnumIntegerField(default=0,
                                                            enum=posts.models.STATUS)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='posts', to='blogs.blog')),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]

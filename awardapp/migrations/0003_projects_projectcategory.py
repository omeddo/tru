# Generated by Django 4.0.4 on 2022-06-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0002_remove_projects_author_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='projectcategory',
            field=models.CharField(default='rw', max_length=80),
        ),
    ]

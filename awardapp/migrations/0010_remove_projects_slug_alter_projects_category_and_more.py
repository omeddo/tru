# Generated by Django 4.0.4 on 2022-06-18 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0009_remove_category_parent_remove_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='slug',
        ),
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.CharField(max_length=80),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

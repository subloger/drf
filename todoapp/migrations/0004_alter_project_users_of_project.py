# Generated by Django 3.2.13 on 2022-06-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_auto_20220602_1947'),
        ('todoapp', '0003_auto_20220610_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='users_of_project',
            field=models.ManyToManyField(blank=True, to='usersapp.User'),
        ),
    ]
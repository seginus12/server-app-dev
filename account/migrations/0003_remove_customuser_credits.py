# Generated by Django 5.0.1 on 2024-01-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='credits',
        ),
    ]
# Generated by Django 2.2.2 on 2020-01-20 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gen', '0004_auto_20200121_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='email',
            new_name='id',
        ),
    ]

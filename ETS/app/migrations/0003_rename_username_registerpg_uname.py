# Generated by Django 4.1.2 on 2022-10-18 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_registerpg_delete_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerpg',
            old_name='username',
            new_name='uname',
        ),
    ]
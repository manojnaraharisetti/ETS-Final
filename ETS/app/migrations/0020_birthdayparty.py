# Generated by Django 4.1.3 on 2022-11-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_delete_birthdayparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdayParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('birthdayname', models.CharField(max_length=200)),
                ('birthdayame', models.CharField(max_length=200)),
                ('birthdayAddress', models.CharField(max_length=200)),
                ('birthdayCity', models.CharField(max_length=200)),
                ('birthdaypcode', models.CharField(max_length=200)),
                ('birthdayprice', models.CharField(max_length=200)),
                ('birthdaymobile', models.CharField(max_length=10)),
                ('birthdayemail', models.CharField(max_length=200)),
            ],
        ),
    ]

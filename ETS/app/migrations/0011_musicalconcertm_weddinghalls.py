# Generated by Django 4.1.2 on 2022-11-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_musicalconcertm_delete_weddinghalls'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicalconcertm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('pcode', models.CharField(max_length=200)),
                ('Tprice', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='weddinghalls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('pcode', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]

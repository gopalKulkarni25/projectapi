# Generated by Django 3.2 on 2022-08-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
    ]

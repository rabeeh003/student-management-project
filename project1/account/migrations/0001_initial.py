# Generated by Django 4.2.6 on 2023-10-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50, unique=True)),
                ('admin_pass', models.CharField(max_length=50)),
                ('admin_mail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='batchs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=10, unique=True)),
                ('batch_year', models.CharField(max_length=10, unique=True)),
                ('batch_teacher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('user_pass', models.CharField(max_length=50)),
                ('user_mail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]

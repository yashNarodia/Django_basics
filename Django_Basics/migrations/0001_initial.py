# Generated by Django 3.2.12 on 2022-04-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('RollNo', models.CharField(max_length=6)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('DOB', models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.IntegerField(primary_key=1, serialize=False)),
                ('empname', models.CharField(max_length=50)),
                ('empemail', models.CharField(max_length=50)),
            ],
        ),
    ]

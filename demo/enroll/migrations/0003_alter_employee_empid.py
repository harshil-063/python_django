# Generated by Django 4.0.3 on 2022-03-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empid',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
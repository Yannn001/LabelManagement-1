# Generated by Django 4.0.6 on 2022-07-18 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_package_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='year_in_school',
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-20 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0012_alter_package_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='upload',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('package_ID', models.TextField(blank=True, null=True)),
                ('tracking_number', models.TextField()),
                ('carrier', models.BooleanField(default=True)),
                ('pic', models.BooleanField(default=True)),
                ('comment', models.BooleanField(default=True)),
                ('date', models.DateField(default=True)),
                ('reciever_initial', models.BooleanField(default=True)),
            ],
        ),
    ]

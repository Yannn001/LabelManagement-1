# Generated by Django 4.0.6 on 2022-07-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_tracknum_alter_package_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='carrier',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='reciever_initial',
            field=models.TextField(max_length=3),
        ),
    ]
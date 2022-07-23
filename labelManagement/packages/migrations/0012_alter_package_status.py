# Generated by Django 4.0.6 on 2022-07-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0011_package_upload_alter_package_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('RE', 'Recieved'), ('DE', 'Delivered')], default='DE', max_length=2),
        ),
    ]

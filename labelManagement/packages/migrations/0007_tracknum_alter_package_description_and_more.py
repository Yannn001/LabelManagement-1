# Generated by Django 4.0.6 on 2022-07-18 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0006_remove_package_id_alter_package_package_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.TextField(max_length=3)),
                ('weekday', models.TextField(max_length=3)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='package',
            name='tracking_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.tracknum'),
        ),
    ]
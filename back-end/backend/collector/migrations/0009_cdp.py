# Generated by Django 2.2.1 on 2019-05-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0008_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255)),
                ('local_int', models.CharField(max_length=255)),
                ('capability', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('port_id', models.CharField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-09 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0010_delete_cdp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='ip_addr',
        ),
    ]

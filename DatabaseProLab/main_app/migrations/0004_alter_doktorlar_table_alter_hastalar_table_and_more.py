# Generated by Django 5.0.4 on 2024-05-15 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='doktorlar',
            table='doktorlar',
        ),
        migrations.AlterModelTable(
            name='hastalar',
            table='hastalar',
        ),
        migrations.AlterModelTable(
            name='sifreler',
            table='sifreler',
        ),
        migrations.AlterModelTable(
            name='yonetici',
            table='yonetici',
        ),
    ]
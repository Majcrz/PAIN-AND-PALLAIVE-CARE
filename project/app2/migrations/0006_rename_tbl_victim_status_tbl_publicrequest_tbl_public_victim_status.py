# Generated by Django 3.2.9 on 2022-02-06 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0005_tbl_publicrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_publicrequest',
            old_name='tbl_victim_status',
            new_name='tbl_public_victim_status',
        ),
    ]

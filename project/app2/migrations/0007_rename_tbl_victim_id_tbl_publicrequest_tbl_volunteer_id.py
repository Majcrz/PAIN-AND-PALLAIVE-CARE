# Generated by Django 3.2.9 on 2022-02-07 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_rename_tbl_victim_status_tbl_publicrequest_tbl_public_victim_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_publicrequest',
            old_name='tbl_victim_id',
            new_name='tbl_volunteer_id',
        ),
    ]
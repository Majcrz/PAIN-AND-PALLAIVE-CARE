# Generated by Django 3.2.9 on 2022-02-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0007_rename_tbl_victim_id_tbl_publicrequest_tbl_volunteer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_volunteer',
            name='tbl_volunteer_password',
            field=models.CharField(default='a', max_length=120),
            preserve_default=False,
        ),
    ]

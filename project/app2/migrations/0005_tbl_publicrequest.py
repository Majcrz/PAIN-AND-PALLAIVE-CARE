# Generated by Django 3.2.9 on 2022-02-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_delete_tbl_publicrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_publicrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tbl_victim_id', models.CharField(max_length=90)),
                ('tbl_request_id', models.CharField(max_length=90)),
                ('tbl_victim_name', models.CharField(max_length=90)),
                ('tbl_victim_address', models.CharField(max_length=90)),
                ('tbl_victim_email', models.CharField(max_length=90)),
                ('tbl_victim_number', models.CharField(max_length=90)),
                ('tbl_request', models.CharField(max_length=90)),
                ('tbl_request_date', models.CharField(max_length=90)),
                ('tbl_victim_status', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'tbl_publicrequest',
            },
        ),
    ]

# Generated by Django 3.2.9 on 2023-09-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_store_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='last_modified',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 3.2.9 on 2023-09-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_store_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 3.2.9 on 2023-09-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20230910_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='html',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

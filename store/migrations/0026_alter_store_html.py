# Generated by Django 3.2.9 on 2023-10-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20231002_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='html',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]

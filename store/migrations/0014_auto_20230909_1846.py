# Generated by Django 3.2.9 on 2023-09-09 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_store_store_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_store',
            new_name='store',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_txt',
            new_name='txt',
        ),
    ]
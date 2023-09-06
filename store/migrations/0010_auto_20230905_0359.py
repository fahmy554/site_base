# Generated by Django 3.2.9 on 2023-09-05 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_post_extra_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store_image',
            name='CompanyImage',
        ),
        migrations.AddField(
            model_name='store',
            name='store_logo',
            field=models.ImageField(blank=True, null=True, upload_to='stores_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='store_image',
            name='Store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store', verbose_name='Store'),
        ),
    ]

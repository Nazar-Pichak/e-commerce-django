# Generated by Django 3.1 on 2024-02-12 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productgalery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductGalery',
            new_name='ProductGallery',
        ),
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'productgallery', 'verbose_name_plural': 'product gallery'},
        ),
    ]
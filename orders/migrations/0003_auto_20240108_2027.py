# Generated by Django 3.1 on 2024-01-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20231224_1411'),
        ('orders', '0002_auto_20240108_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]

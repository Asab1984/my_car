# Generated by Django 4.2.6 on 2023-11-18 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукти'},
        ),
    ]
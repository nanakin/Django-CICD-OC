# Generated by Django 3.0 on 2024-01-12 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_copy_lettings_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
    ]

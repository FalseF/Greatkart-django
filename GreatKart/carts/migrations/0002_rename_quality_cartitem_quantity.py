# Generated by Django 3.2.4 on 2021-08-05 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quality',
            new_name='quantity',
        ),
    ]
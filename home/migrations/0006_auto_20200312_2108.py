# Generated by Django 3.0.3 on 2020-03-12 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_sites_indexed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uncrawled',
            old_name='root',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='uncrawled',
            name='links',
        ),
    ]
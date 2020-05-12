# Generated by Django 3.0.3 on 2020-04-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_search_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexerSecondary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=255)),
                ('key1', models.CharField(max_length=50)),
                ('key2', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='indexing',
            name='site_id',
            field=models.CharField(max_length=255),
        ),
    ]
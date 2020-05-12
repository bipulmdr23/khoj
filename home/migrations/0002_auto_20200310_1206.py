# Generated by Django 3.0.3 on 2020-03-10 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='indexing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.TextField()),
                ('key', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='sites',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sites',
            name='domain',
            field=models.CharField(default='.com', max_length=20),
        ),
        migrations.AddField(
            model_name='sites',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]

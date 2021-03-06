from django.db import models
from django.contrib import admin
from django.utils import timezone

class indexingAdmin(admin.ModelAdmin):
    search_fields = ['key']


class sites(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=400)
    domain = models.CharField(max_length=20, default='.com')
    display = models.BooleanField(default=True)
    visit_count = models.IntegerField(default=0)
    priority = models.FloatField(default=1.0000)
    indexed = models.BooleanField(default=False)
    reference_dir = models.TextField(max_length=255, default='khoj_contents/content1')
    file_name = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.title


class uncrawled(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class indexing(models.Model):
    site_id = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.key


class IndexerSecondary(models.Model):
    site_id = models.CharField(max_length=255)
    key1 = models.CharField(max_length=50)
    key2 = models.CharField(max_length=50)

    def __str__(self):
        return self.key1 + ' ' + self.key2


class feedback(models.Model):
    time=timezone.now()
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    desc=models.TextField()
    report_date=models.DateField(default = time)

    def __str__(self):
        return self.name + " : "+self.email


class search_text(models.Model):
    search_text = models.CharField(max_length=255)
    visit_couont = models.IntegerField(default=0)
    priority = models.FloatField(default=1.0)

    def __str__(self):
        return self.search_text


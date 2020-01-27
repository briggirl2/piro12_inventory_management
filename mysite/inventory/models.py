from django.db import models
from django.urls import reverse

from mysite.utils import uuid_upload_to


class Company(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    remain = models.PositiveIntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inventory:item_detail', kwargs={'pk': self.pk})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class Buildings(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='GID')
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=40)
    building_type = models.CharField(max_length=40)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.address

class CustomUserModel(AbstractUser):

    username = models.CharField(max_length=150, primary_key=True)

    Morasko = "Morasko"
    Piatkowo = "Piatkowo"

    district_choices = (
    (Morasko, "Morasko"),
    (Piatkowo, "Piątkowo"),
    )

    district = models.CharField(max_length=15, choices=district_choices, default=Morasko)
    address = models.OneToOneField(Buildings, on_delete=models.CASCADE, null=True, blank=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

class Announcement(models.Model):

    announcement = 'announcement'
    alert = 'alert'
    offer ='offer'

    announcement_types = (
    (announcement, 'Announcement'),
    (alert, 'Alert'),
    (offer, 'Offer'),
    )

    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    text = models.CharField(max_length=1500, null=False, blank=False)
    announcement_type = models.CharField(max_length=12, choices=announcement_types, default=announcement)
    user_name = models.ForeignKey(CustomUserModel, db_column='user_name', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    building_id = models.ForeignKey(Buildings, db_column='building_id', on_delete=models.CASCADE)

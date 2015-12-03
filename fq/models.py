from django.db import models


class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20)


class Regions(models.Model):
    id = models.AutoField(primary_key=True)
    cities_id = models.ForeignKey(Cities)
    region = models.CharField(max_length=20)


class Venues(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45, null=True, blank=True)
    city = models.CharField(max_length=45, null=True, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    regions_id = models.ForeignKey(Regions)


class Tips(models.Model):
    id = models.AutoField(primary_key=True)
    venues_id = models.ForeignKey(Venues)
    text = models.CharField(max_length=200)


class Texts(models.Model):
    id = models.AutoField(primary_key=True)
    tips_id = models.ForeignKey(Tips)
    word = models.CharField(max_length=25)



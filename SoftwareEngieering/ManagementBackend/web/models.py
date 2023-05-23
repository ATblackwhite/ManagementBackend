# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CulturalRelicsData(models.Model):
    id = models.IntegerField(primary_key=True)
    object_name = models.CharField(max_length=255, blank=True, null=True)
    cat1 = models.CharField(max_length=255, blank=True, null=True)
    cat2 = models.CharField(max_length=255, blank=True, null=True)
    cat3 = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    makers_name = models.CharField(max_length=255, blank=True, null=True)
    museum = models.CharField(max_length=255, blank=True, null=True)
    time_period = models.CharField(max_length=255, blank=True, null=True)
    object_type = models.CharField(max_length=255, blank=True, null=True)
    provenance = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    previous_owner = models.CharField(max_length=255, blank=True, null=True)
    geography = models.CharField(max_length=255, blank=True, null=True)
    medium = models.CharField(max_length=255, blank=True, null=True)
    dimensions = models.CharField(max_length=255, blank=True, null=True)
    credit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cultural_relics_data'


class User(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_password = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_sex = models.IntegerField(blank=True, null=True)
    user_tel = models.CharField(max_length=255, blank=True, null=True)
    user_comment = models.IntegerField(blank=True, null=True)
    user_login = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Collections(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    collection_name = models.CharField(db_column='Collection_name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    museum = models.CharField(db_column='Museum', max_length=200, blank=True, null=True)  # Field name made lowercase.
    materials = models.CharField(db_column='Materials', max_length=200, blank=True, null=True)  # Field name made lowercase.
    creation_date = models.CharField(db_column='Creation_date', max_length=200, blank=True, null=True)  # Field name made lowercase.
    discription = models.CharField(db_column='Discription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_url', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'collections'

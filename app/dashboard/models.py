# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class DoctorGroup(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='doctor_groups')
    patients = models.ManyToManyField('HospPatients', related_name='doctor_groups')


class HospPatients(models.Model):
    subject_id = models.TextField(blank=True, null=False, primary_key=True)
    gender = models.TextField(blank=True, null=True)
    anchor_age = models.TextField(blank=True, null=True)
    anchor_year = models.TextField(blank=True, null=True)
    anchor_year_group = models.TextField(blank=True, null=True)
    dod = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hosp/patients'
        app_label = 'dashboard'

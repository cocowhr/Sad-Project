# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital)


class User(models.Model):
    name = models.CharField(max_length=10)
    passwd = models.CharField(max_length=6)
    contact = models.CharField(max_length=50)


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    fee = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    contact = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)


class Appointment(models.Model):
    appointment_date = models.TimeField
    create_date = models.TimeField(auto_now=True)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)
    user = models.ForeignKey(User)


class Order(models.Model):
    fare = models.FloatField()
    appointment = models.ForeignKey(Appointment)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)
    user = models.ForeignKey(User)



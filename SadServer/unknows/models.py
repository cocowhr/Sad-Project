# -*- coding: utf-8 -*-

from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital)


class User(models.Model):
    name = models.CharField(max_length=10)
    passwd = models.p(max_length=6)
    contact = models.CharField(max_length=50)


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    contact = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)


class Order(models.Model):
    fare = models.FloatField(max_digits=6, decimal_places=6)
    appointment = models.ForeignKey(Appointment)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)
    user = models.ForeignKey(User)


class Appointment(models.Model):
    appointment_date = models.TimeField
    create_date = models.TimeField(auto_now=True)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)
    user = models.ForeignKey(User)

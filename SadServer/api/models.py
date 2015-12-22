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
    idcard = models.CharField(max_length=50)
    realname = models.CharField(max_length=10)
    verify = models.BooleanField(default=False)
    credit = models.IntegerField(default=5)
    admin = models.BooleanField(default=False)


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    fee = models.IntegerField()
    gender = models.CharField(max_length=6)
    contact = models.CharField(max_length=50)
    limit = models.IntegerField(default=0)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)


class Appointment(models.Model):
    appointment_date = models.DateField()
    date2 = models.CharField(max_length=6)
    fare = models.FloatField()
    create_date = models.DateField(auto_now=True)
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)
    user = models.ForeignKey(User)


class Order(models.Model):
    appointment_date = models.DateField()
    date2 = models.CharField(max_length=6)
    pay_date = models.DateField(auto_now=True)
    fare = models.FloatField()
    create_date = models.DateField()
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)
    user = models.ForeignKey(User)


class Maxium_Appointment(models.Model):
    hospital = models.ForeignKey(Hospital)
    department = models.ForeignKey(Department)
    doctor = models.ForeignKey(Doctor)  # 医生
    date = models.DateField()  # 日期
    date2 = models.CharField(max_length=6)
    number = models.IntegerField(default=0)  # 当天的最大预约人数

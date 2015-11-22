# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('create_date', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('contact', models.CharField(max_length=50)),
                ('department', models.ForeignKey(to='api.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fare', models.FloatField()),
                ('appointment', models.ForeignKey(to='api.Appointment')),
                ('department', models.ForeignKey(to='api.Department')),
                ('doctor', models.ForeignKey(to='api.Doctor')),
                ('hospital', models.ForeignKey(to='api.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('passwd', models.CharField(max_length=6)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='api.User'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(to='api.Hospital'),
        ),
        migrations.AddField(
            model_name='department',
            name='hospital',
            field=models.ForeignKey(to='api.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='department',
            field=models.ForeignKey(to='api.Department'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(to='api.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(to='api.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(to='api.User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0011_house_guest'),
        ('wishlist', '0001_initial'),
        ('member', '0008_auto_20170815_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='like_houses',
            field=models.ManyToManyField(related_name='wishlist_info', through='wishlist.Wishlist', to='house.House'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.EmailField(max_length=254),
        ),
    ]

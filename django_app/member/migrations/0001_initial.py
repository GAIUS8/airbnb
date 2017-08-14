# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import member.models.users


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('img_profile', models.ImageField(blank=True, upload_to='user')),
                ('gender', models.CharField(choices=[('MALE', '남자'), ('FEMALE', '여자'), ('OTHER', '기타')], default='OTHER', max_length=10)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('preference_language', models.CharField(blank=True, max_length=20, null=True)),
                ('preference_currency', models.CharField(blank=True, max_length=20, null=True)),
                ('living_site', models.CharField(blank=True, max_length=100, null=True)),
                ('introduce', models.TextField(blank=True, max_length=300, null=True)),
                ('username', models.EmailField(max_length=254)),
                ('identifier', models.CharField(default=member.models.users.f, max_length=40, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]

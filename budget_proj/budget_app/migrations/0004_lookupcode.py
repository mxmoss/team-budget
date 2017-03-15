# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0003_budgethistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookupCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code_type', models.CharField(default='', max_length=32)),
                ('code', models.CharField(default='', max_length=32)),
                ('description', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
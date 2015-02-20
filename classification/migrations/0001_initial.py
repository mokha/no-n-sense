# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=65535)),
                ('predicted_category', models.CharField(max_length=5)),
                ('predicted_rate', models.IntegerField()),
                ('is_positive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_category_accurate', models.BooleanField()),
                ('is_rate_accurate', models.BooleanField()),
                ('is_positivity_accurate', models.BooleanField()),
                ('by_user', models.BooleanField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='is_positivity_accurate',
            field=models.NullBooleanField(),
        ),
    ]

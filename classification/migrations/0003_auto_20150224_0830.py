# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0002_auto_20150220_1521'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classifications',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='is_category_accurate',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='is_positivity_accurate',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='is_rate_accurate',
        ),
        migrations.AddField(
            model_name='statistics',
            name='category',
            field=models.BooleanField(choices=[(1, b''), (0, b'')], default=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='positivity',
            field=models.BooleanField(choices=[(1, b''), (0, b'')], default=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='rate',
            field=models.BooleanField(choices=[(1, b''), (0, b'')], default=True),
        ),
        migrations.AddField(
            model_name='statistics',
            name='rate_nlp',
            field=models.BooleanField(choices=[(1, b''), (0, b'')], default=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='by_user',
            field=models.BooleanField(default=True),
        ),
    ]

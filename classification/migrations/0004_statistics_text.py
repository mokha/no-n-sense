# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classification', '0003_auto_20150224_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='text',
            field=models.CharField(default=b'', max_length=65535, unique=True),
        ),
    ]

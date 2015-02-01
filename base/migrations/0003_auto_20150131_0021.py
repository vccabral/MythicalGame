# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150130_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='estimated_man_months',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='estimated_methods',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='estimated_objects',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='estimated_test_cases',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

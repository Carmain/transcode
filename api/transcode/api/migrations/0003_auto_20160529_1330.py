# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 13:30
from __future__ import unicode_literals

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_transcodefile_uploadsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcodefile',
            name='rawFile',
        ),
        migrations.AddField(
            model_name='transcodefile',
            name='fileType',
            field=models.CharField(choices=[(b'mvk', b'Mastroska'), (b'png', b'PNG Image'), (b'tmp', b'Temporary')], default=b'tmp', max_length=3),
        ),
        migrations.AddField(
            model_name='transcodefile',
            name='uuid',
            field=models.CharField(default=api.models.generate_uuid4, max_length=32),
        ),
    ]

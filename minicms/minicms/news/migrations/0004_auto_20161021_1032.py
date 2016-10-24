# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20161021_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='Content',
            field=DjangoUeditor.models.UEditorField(default='test', verbose_name='\u5185\u5bb9', blank=True),
        ),
    ]

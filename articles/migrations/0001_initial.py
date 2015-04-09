# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(max_length=200)),
                ('article_author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('article_category', models.CharField(max_length=200)),
                ('article_hero', models.ImageField(upload_to=b'')),
                ('article_img', models.ImageField(upload_to=b'')),
                ('article_body', models.TextField()),
            ],
        ),
    ]

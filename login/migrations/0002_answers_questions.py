# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('answer', models.CharField(max_length=200)),
                ('score', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
    ]

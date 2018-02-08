# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('respuesta', models.CharField(max_length=100)),
                ('puntaje', models.IntegerField()),
            ],
            options={
                'db_table': 'respuestas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rin',
            fields=[
                ('usuario', models.CharField(primary_key=True, max_length=30, serialize=False)),
                ('password', models.CharField(max_length=30, blank=True, null=True)),
            ],
            options={
                'db_table': 'rin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tlogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('ganancia', models.IntegerField()),
            ],
            options={
                'db_table': 'tlogin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Trivias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('trivia', models.CharField(max_length=250)),
                ('opcion1', models.CharField(max_length=100)),
                ('opcion2', models.CharField(max_length=100)),
                ('opcion3', models.CharField(max_length=100)),
                ('opcion4', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'trivias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuariotrivia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('idprincipal', models.IntegerField()),
                ('puntos', models.IntegerField()),
                ('triviaid', models.ForeignKey(to='login.Trivias')),
                ('usuarioid', models.ForeignKey(to='login.Tlogin')),
            ],
            options={
                'db_table': 'usuariotrivia',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='respuestas',
            name='idtrivias',
            field=models.ForeignKey(to='login.Trivias'),
        ),
        migrations.AlterUniqueTogether(
            name='usuariotrivia',
            unique_together=set([('idprincipal', 'usuarioid', 'triviaid')]),
        ),
    ]

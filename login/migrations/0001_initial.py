# Generated by Django 2.0.1 on 2018-02-05 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('usuario', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'rin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idprincipal', models.IntegerField()),
                ('puntos', models.IntegerField()),
                ('triviaid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Trivias')),
                ('usuarioid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Tlogin')),
            ],
            options={
                'db_table': 'usuariotrivia',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='respuestas',
            name='idtrivias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Trivias'),
        ),
        migrations.AlterUniqueTogether(
            name='usuariotrivia',
            unique_together={('idprincipal', 'usuarioid', 'triviaid')},
        ),
    ]

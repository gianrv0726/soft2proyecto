from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Tlogin(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    ganancia = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'tlogin'



class Rin(models.Model):
    usuario = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rin'

class Trivias(models.Model):
    trivia = models.CharField(max_length=250)
    opcion1 = models.CharField(max_length=100)
    opcion2 = models.CharField(max_length=100)
    opcion3 = models.CharField(max_length=100)
    opcion4 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'trivias'


class Respuestas(models.Model):
    respuesta = models.CharField(max_length=100)
    idtrivias = models.ForeignKey('Trivias', on_delete=models.CASCADE,)
    puntaje = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'respuestas'
####
class Usuariotrivia(models.Model):
    idprincipal = models.IntegerField()
    usuarioid = models.ForeignKey('Tlogin', on_delete=models.CASCADE,)
    triviaid = models.ForeignKey('Trivias', on_delete=models.CASCADE,)
    puntos = models.IntegerField()


    class Meta:
        managed = True
        unique_together = (('idprincipal', 'usuarioid', 'triviaid'),)
        db_table = 'usuariotrivia'

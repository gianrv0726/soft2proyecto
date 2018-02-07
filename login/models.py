from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime



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

###trivias
class questions(models.Model):
    question = models.CharField(max_length=250)
    #body = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Questions"

class answers(models.Model):
    answer = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    def __str__(self):
        return self.answer
    class Meta:
        verbose_name_plural = "Answers"

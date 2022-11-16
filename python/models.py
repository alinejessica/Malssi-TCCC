from email.utils import parsedate_to_datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    sobrenome = models.CharField(max_length=16)

class Comentario(models.Model):
    comentario = models.TextField(max_length=255)
    usuario = models.ForeignKey(Usuario,on_delete = models CASCADE)


class produtos(models.Model):
    
class pedidos(models.Model):












#PROMP DE COMANDO
#cd pasta 
#python manage.py migrate
#python manage.py  migrations(apagar)



#colocar no mysql:::
#create database


# mysql- usuario_id  tirei foto das colunas no msql 

#select * from seuapp_usuario where usuario = "teste001"
#select * from seuapp_comentario

#delete from django_migrations where id = 20
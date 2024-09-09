from peewee import AutoField, CharField, DateField, ForeignKeyField, Model
from basedato.db import db


class Curso(Model):
    id = AutoField()
    nombre = CharField()
    descripcion = CharField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    horas = CharField()

    class Meta:
       database = db
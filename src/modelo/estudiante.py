from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model
from basedato.db import db
from modelo.curso import Curso
class Estudiante(Model):
    id = AutoField()
    nombre = CharField()
    dni = CharField()
    correo_electronico = CharField()
    numero_telefono = CharField()
    fecha_nacimiento = DateField()
    curso_id = ForeignKeyField(Curso)

    class Meta:
       database = db
       tabla_name = "Estudiante"




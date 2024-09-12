from modelo.estudiante import Estudiante
from modelo.curso import Curso

class EstudiantesServicio():

    @staticmethod
    def crear_estudiante(id, nombre, dni, correo_electronico, numero_telefono, fecha_nacimiento, curso_id):
        curso = Curso.get(Curso.id == curso_id)
        estudiante = Estudiante.create(id=id, nombre=nombre, dni=dni, correo_electronico=correo_electronico, numero_telefono=numero_telefono, fecha_nacimiento=fecha_nacimiento, curso_id=curso)
        return estudiante

    @staticmethod
    def eliminar_estudiante(id):
        estudiante = Estudiante.get(Estudiante.id == id) 
        estudiante.delete_instance()
        return estudiante   

    @staticmethod
    def mostrar_estudiante():
        return list(Estudiante.select())

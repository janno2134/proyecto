from basedato.db import db
from modelo.curso import Curso
from modelo.estudiante import Estudiante
from controlador.curso_controlador import CursoControlador
def main():
    db.connect()
    #db.create_tables([Curso, Estudiante])

    CursoControlador.crear("programacion III","trabajadr","2024-09-24","2024-10-24","12:00" )

    cursos = CursoControlador.mostrar()
    if cursos:
        for curso in cursos:
            print(f"Curso: {curso.id} - {curso.nombre}")
    else:
        print("no hay cursos disponibles. ")

    EstudianteControlador.crear("Jano Bagdadi","12345678","janobagdadi@gmail.com","2901323470","2006-10-10",1)

    estudiante = EstudianteControlador.mostrar()
    if estudiante:
        for estudiante in estudiante
            print(f"Estudiante: {estudiante.id} - {esudiante.nombre}")
    else:
        print("no hay estudiantes")

    CursoControlador.eliminar(1)    

if __name__ == "__main__":
    main()
from servicio.estudiante_servicio import EstudianteServicio

class EstudianteControlador():

    def crear(id, nombre, dni, correo_electronico, numero_telefono, fecha_nacimiento, curso_id):
        return EstudianteControlador.crear_estudiante(id, nombre, dni, correo_electronico, numero_telefono, fecha_nacimiento, curso_id)

    def mostrar():
        return EstudianteControlador.mostrar_estudiante()    
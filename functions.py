estudiantes = []
estado = ("activo", "inactivo")


def buscar_estudiante(id_est):
    for est in estudiantes:
        if est["id"] == id_est:
            return est
    return None


def registrar_estudiante():
    id_est = input("ingrese id: ")

    if buscar_estudiante(id_est):
        print("ya existe")
        return

    nombre = input("ingresa nombre: ")
    edad = int(input("ingresa la edad: "))
    programa = input("ingrese el programa: ")
    estado_est = input("ingrese estado(activo/inactivo): ")

    nuevo_estudiante = {
        "nombre": nombre,
        "id": id_est,
        "edad": edad,
        "programa": programa,
        "estado": estado_est
    }

    estudiantes.append(nuevo_estudiante)
    print("agregado")


def mostrar_estudiantes():
    if not estudiantes:
        print("no hay estudiantes")
    else:
        for est in estudiantes:
            print(est)


def consultar_estudiante():
    id_est = input("ingrese id para buscar: ")
    est = buscar_estudiante(id_est)

    if est:
        print(est)
    else:
        print("no encontrado")


def actualizar_estudiantes():
    id_est = input("ingrese id para actualizar: ")
    est = buscar_estudiante(id_est)

    if est:
        est["nombre"] = input("nuevo nombre: ")
        est["programa"] = input("nuevo programa: ")

        try:
            est["edad"] = int(input("nueva edad: "))
        except:
            print("edad invalida")

        nuevo_estado = input("nuevo estado: ")
        if nuevo_estado in estado:
            est["estado"] = nuevo_estado

        print("actualizado")
    else:
        print("no encontrado")


def eliminar_estudiantes():
    id_est = input("ingrese id para eliminar: ")
    est = buscar_estudiante(id_est)

    if est:
        estudiantes.remove(est)
        print("eliminado")
    else:
        print("no encontrado")


from functions import *

def menu():
    print("menu:")
    print("1. registrar")
    print("2. mostrar")
    print("3. consultar")
    print("4. buscar")
    print("5. actualizar")
    print("6. eliminar")
    print("7. salir")




def main():
    while True:
        menu()
        opcion = input("ingresa opcion que desea realizar: ")


        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            consultar_estudiante()
        
        elif opcion == "4":
            buscar_estudiante()

        elif opcion == "5":
            actualizar_estudiantes()

        elif opcion == "6": 
            eliminar_estudiantes()


        else:
            print("saliendo")
            break


main()
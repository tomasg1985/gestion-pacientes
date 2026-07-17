from logica_sistema import *
from colorama import Fore, Back, Style, init
init(autoreset=True)

print()
print("1. Agregar nuevo paciente")
print("2. Más opciones")
print("Salir")
print()

opcion_menu: str = input("Elija una opción del menú: ").strip()

match opcion_menu:
    
    #### Menu principal CRUD
    
    case "1":
        nuevo_paciente()
    
    case "2":
        
        #### Mas opciones: Submenu para turnos e historias_clinicas

        print()
        print("1. Nuevo turno")
        print("2. Historia clinica")
        print("Salir")
        print()

        opcion_submenu: str = input("Elija una opción del menú:  ").strip().title()

        match opcion_submenu:
            case "1":
                print()
                print("====NUEVO TURNO MÉDICO ====")
                print()
                
                nuevo_turno()

            case "2":
                print()
                print("==== HISTORIAS CLÍNICAS ====")
                print()
                
                nueva_historia()

            case _:
                print("=== Opción no válida ===")

    case _:
        print("=== Opción no válida ===")

conexion.close()
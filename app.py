from logica_sistema import *
from colorama import Fore, Back, Style, init
init(autoreset=True)

print()
print("1. Agregar nuevo paciente")
print("Salir")
print()

opcion_menu: str = input("Elija una opción del menú: ").strip()

match opcion_menu:
    
    case "1":
        nuevo_paciente()
    case _:
        print("=== Opción inválida ===")

conexion.close()
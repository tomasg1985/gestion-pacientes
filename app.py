from logica_sistema import *
from colorama import Fore, Back, Style, init
init(autoreset=True)


### MENÚ PRINCIPAL

print()
print("1. Area profesional")
print("2. Area paciente")
print("3. Area administrativa")
print("4. Salir")
print()

opcion_menu: str = input("Elija una opción del menú: ").strip()

### MENÚ PROFESIONAL

match opcion_menu:
    
    case "1":
        print()
        print("==== AREA PROFESIONAL ====")
        print()
        print("==== MENÚ ====")
        print()
        print("1. Agregar turno")
        print("2. Ver paciente")
        print("3. Actualizar historia")
        print("4. Eliminar paciente")
        print("5. Más opciones")
        print("6. Salir")
        print()
        
        opcion_submenu_profesional: str = input("Elija una opción del menú:  ").strip().title()
        print()

        match opcion_submenu_profesional:
            case "1":
                print()
                print("====NUEVO TURNO MÉDICO ====")
                print()
                
                nuevo_turno()
            
            case "2":
                print()
                print("==== VER PACIENTE ====")
                print()
                
                ver_pacientes_profesional()
            
            case "3":
                print()
                print("==== ACTUALIZAR HISTORIA ====")
                print()
                
                print("Opción en desarrollo...")
                
            case "4":
                print()
                print("==== ELIMINAR PACIENTE ====")
                print()
                
                print("Opción en desarrollo...")
                
                ## MAS OPCIONES
            
            case "5":
                
                print()
                print("1. Nueva historia")
                print("2. Nuevo paciente")
                print("Salir")
                print()
                
                mas_opciones_prof: str = input("Elija una opción: ").strip()
                print()
                
                match mas_opciones_prof:
                    case "1":
                        print()
                        print("==== NUEVA HISTORIA ====")
                        print()
                        
                        nueva_historia()
                    
                    case "2":
                        print()
                        print("==== NUEVO PACIENTE ====")
                        print()
                        
                        nuevo_paciente()
                    
            case "6":
                print("Sistema cerrado...")
            
            case _:
                print("=== Opción no válida ===")
                
    
### MENÚ PACIENTE
    
    case "2":
        print()
        print("==== AREA PACIENTE ====")
        print()
        print("==== MENÚ ====")
        print()
        print("1. Ver turno")
        print("2. Salir")
        print()
        
        opcion_submenu_paciente: str = input("Elija una opción del menú:  ").strip().title()
        print()
    
        match opcion_submenu_paciente:
            case "1":
                print()
                print("==== VER TURNO ====")
                print()
                
                print("Opción en desarrollo...")
            
            case "2":
                print("Sistema cerrado...")
                

### MENÚ ADMINISTRATIVO

    case "3":
        
        print()
        print("==== AREA ADMINISTRATIVA ====")
        print()
        print("==== MENÚ ====")
        print()
        print("1. Nuevo profesional")
        print("2. Salir")
        print()
        
        opciones_admin: str = input("Elija una opción: ").strip()
        print()
        
        match opciones_admin:
            case "1":
                print()
                print("==== AGREGAR NUEVO PROFESIONAL ====")
                print()
                
                nuevo_profesional()
                
            case "2":
                print("Sistema cerrado...")
                
    case "4":
        print("Sistema cerrado...")
        
    case _:
        print("=== Opción no válida ===")
        
conexion.close()
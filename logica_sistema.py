### DESARROLLAMOS UN SISTEMA COMPLETO DE GESTION DE PACIENTES, ASIGNACION DE TURNOS, SEGUIMIENTO Y MANEJO DE HISTORIAS CLINICAS.

import sqlite3
import datetime
#### El sistema es un CRUD como funcionalidad principal

conexion = sqlite3.connect("registro_pacientes.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes(
        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_nacimiento TEXT NOT NULL,
        correo_electronico TEXT NOT NULL,
        telefono INTEGER NOT NULL,
        documento_identidad INTEGER NOT NULL,
        contacto_emergencia INTEGER NOT NULL,
        fecha_consulta TEXT NOT NULL
    )
''')
conexion.commit()

def nuevo_paciente():
    while True:
        
        nuevo_paciente: str = input("¿Deseas agregar un nuevo paciente? Si / No (Escriba Salir para cancelar la operación): ").strip().title()
        
        if nuevo_paciente == "Salir" or nuevo_paciente == "No":
            print("==== Operacion cancelada o finalizada ====")
            break

        if nuevo_paciente == "Si":
            
            nombre: str = input("Nombre: ").strip().title()

            if nombre == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            apellido: str = input("Apellido: ").strip().title()

            if apellido == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            fecha_nacimiento: str = input("Fecha de nacimiento (AAAA-MM-DD): ")

            if fecha_nacimiento == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            correo_electronico: str = input("E-mail: ").strip().title()

            if correo_electronico == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            try:
                telefono: int = int(input("Telefono: "))
                documento_identidad: int = int(input("D.N.I: "))
                contacto_emergencia: int = int(input("Contacto de emergencia: "))
            except ValueError:
                print("¡Error! Teléfono, DNI y Contacto deben ser solo números enteros.")
                continue
            
            fecha_consulta = datetime.datetime.now().strftime("%c")
            print(fecha_consulta)
            
    cursor.execute('INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, correo_electronico, telefono, documento_identidad, contacto_emergencia, fecha_consulta) VALUES (?,?,?,?,?,?,?,?)', (nombre, apellido, fecha_nacimiento, correo_electronico, telefono, documento_identidad, contacto_emergencia, fecha_consulta))
    conexion.commit()
    
    print()
    print("==== PACIENTE REGISTRADO CON ÉXITO ====")
    print()
    print(f"Nombre y Apellido: {nombre} {apellido} \n")
    print()
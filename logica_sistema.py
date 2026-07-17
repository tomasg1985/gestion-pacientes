### DESARROLLAMOS UN SISTEMA COMPLETO DE GESTION DE PACIENTES, ASIGNACION DE TURNOS, SEGUIMIENTO Y MANEJO DE HISTORIAS CLINICAS.

import sqlite3
import datetime
#### El sistema es un CRUD como funcionalidad principal

conexion = sqlite3.connect("registro_pacientes.db")
cursor = conexion.cursor()

#### Tabla datos estáticos clientes "pacientes"

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

#### Tabla datos estáticos clientes "turnos"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS turnos(
        id_turno INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER NOT NULL,
        fecha_turno TEXT NOT NULL,
        hora_turno TEXT NOT NULL,
        estado TEXT NOT NULL DEFAULT 'Pendiente',
        FOREIGN KEY(id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE
    )
''')
conexion.commit()

#### Tabla datos estáticos clientes "historias_clinicas"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS historias_clinicas(
        id_historia INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER NOT NULL,
        fecha_registro TEXT NOT NULL,
        motivo_consulta TEXT NOT NULL,
        diagnostico TEXT NOT NULL,
        tratamiento TEXT NOT NULL,
        FOREIGN KEY(id_paciente) REFERENCES pacientes(id_paciente) ON DELETE CASCADE
    )
''')
conexion.commit()


# AGREGAR NUEVO PACIENTE

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
            
            correo_electronico: str = input("E-mail: ").strip()
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
    
    
# AGREGAR NUEVO TURNO
    
def nuevo_turno():
    while True:
        
        registrar_turno: str = input("¿Deseas agendar un nuevo paciente? Si / No (Escriba Salir para cancelar la operación): ").strip().title()
        
        if registrar_turno == "Salir" or registrar_turno == "No":
            print("==== Operacion cancelada o finalizada ====")
            break
        
        if registrar_turno == "Si":
            
            try:
                dni: int = int(input("D.N.I: "))
            except ValueError:
                print("¡Error! El DNI debe ser solo números enteros.")
                continue
            
            cursor.execute('SELECT id_paciente, nombre, apellido FROM pacientes WHERE documento_identidad = ?', (dni,))
            paciente = cursor.fetchone()
            conexion.commit()
            
            id_paciente, nombre, apellido = paciente
            print(f"Paciente seleccionado: {nombre} {apellido}")
            
            fecha_turno: str = input("Fecha del turno (AAAA-MM-DD): ").strip()
            if fecha_turno == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            hora_turno: str = input("Hora del turno (HH:MM): ").strip()
            if hora_turno == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            print("Estados del turno:")
            print()
            print("1. Pendiente")
            print("2. Confirmado")
            print("3. En Sala de Espera")
            print("4. Atendido")
            print("5. Cancelado")
            print("6. Ausente")
            print()
            
            estado: str = input("Estado del turno (1-6): ").strip()
            if estado == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            if estado == "1":
                estado = "Pendiente"
            elif estado == "2":
                estado = "Confirmado"
            elif estado == "3":
                estado = "En Sala de Espera"
            elif estado == "4":
                estado = "Atendido"
            elif estado == "5":
                estado = "Cancelado"
            elif estado == "6":
                estado = "Ausente"
            else:
                print("==== Opción no válida ====")

    cursor.execute('INSERT INTO turnos (id_paciente, fecha_turno, hora_turno, estado) VALUES (?,?,?,?)', (id_paciente, fecha_turno, hora_turno, estado))
    conexion.commit()
    
    print()
    print("==== TURNO CONFIRMADO ====")
    print()
    print(f"Nombre y Apellido: {nombre} {apellido}")
    print(f"Fecha: {fecha_turno}")
    print(f"Hora: {hora_turno}")
    print(f"Estado: {estado}")
    print("=" * 40 + "\n")
    print()
    
    
# AGREGAR NUEVA HISTORIA MÉDICA

def nueva_historia():
    
    while True:
        
        historia_paciente: str = input("¿Deseas agendar una nueva historia para el paciente? Si / No (Escriba Salir para cancelar la operación): ").strip().title()
        
        if historia_paciente == "Salir" or historia_paciente == "No":
            print("==== Operación cancelada o finalizada ====")
            break
        
        if historia_paciente == "Si":
            
            try:
                dni = int(input("Ingrese el D.N.I del paciente: "))
            except ValueError:
                print("¡Error! El DNI debe ser solo números enteros.")
                continue
            
            cursor.execute(
                "SELECT id_paciente, nombre, apellido FROM pacientes WHERE documento_identidad = ?",
                (dni,),
            )
            paciente = cursor.fetchone()
            conexion.commit()
            
            if not paciente:
                print(f"¡Error! No existe ningún paciente registrado con el DNI {dni}.")
                print("Primero debes registrar al paciente en el menú de Pacientes.")
                continue
            
            id_paciente, nombre, apellido = paciente
            print(f"Paciente seleccionado: {nombre} {apellido}")
            
            fecha_registro: str = input("Fecha de registro del paciente (AAAA-MM-DD) [Enter para hoy]: ")
            if not fecha_registro:
                fecha_registro = datetime.datetime.today().strftime("%Y-%m-%d")
            
            motivo_consulta: str = input("Motivo de su consulta: ").strip()
            if motivo_consulta == "":
                print("Este campo no puede quedar vacío.")
                continue
        
            diagnostico: str = input("Diagnostico: ").strip()
            if diagnostico == "":
                print("Este campo no puede quedar vacío.")
                continue
            
            tratamiento: str = input("Tratamiento: ").strip()
            if tratamiento == "":
                print("Este campo no puede quedar vacío.")
                continue
    
    cursor.execute('INSERT INTO historias_clinicas (id_paciente, fecha_registro, motivo_consulta, diagnostico, tratamiento) VALUES (?,?,?,?,?)', (id_paciente, fecha_registro, motivo_consulta, diagnostico, tratamiento))
    conexion.commit()

            
    print()
    print("==== HISTORIA AGREGADA ====")
    print()
    print(f"Nombre y Apellido: {nombre} {apellido}")
    print(f"Registrado: {fecha_registro}")
    print(f"Motivo de la consulta: {motivo_consulta}")
    print(f"Diagnóstico: {diagnostico}")
    print(f"Tratamiento: {tratamiento}")
    print("=" * 40 + "\n")
    print()
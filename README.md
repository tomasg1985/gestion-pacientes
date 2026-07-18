# 🏥 Sistema de Gestión de Pacientes e Historias Médicas (Python & SQLite3)

<p align="left">
  <img src="https://shields.io" alt="Language">
  <img src="https://shields.io" alt="Repo Size">
  <img src="https://shields.io" alt="Stars">
</p>

Un ecosistema digital backend diseñado para optimizar la administración clínica, el seguimiento de pacientes y la asignación inteligente de turnos médicos. El sistema implementa una arquitectura híbrida avanzada que combina la persistencia relacional con estructuras de datos eficientes en memoria.

---

### 🚀 Características Técnicas y Funcionalidades

*   **Persistencia Relacional Avanzada (SQLite3):** Almacenamiento estructurado de datos que garantiza la integridad, consistencia y persistencia a largo plazo de las historias clínicas y agendas de turnos.
*   **Gestión del Ciclo Médico (CRUD Completo):** Módulo centralizado para el registro de pacientes, actualización de fichas médicas, seguimiento evolutivo e historial de consultas.
*   **Asignación de Turnos Dinámica:** Motor lógico para el control, agendamiento y ordenamiento cronológico de citas médicas, previniendo la superposición de horarios.
*   **Programación Defensiva y Sanitización:** Capa de validación estricta para evitar la inyección de datos corruptos, campos obligatorios vacíos o inconsistencias de formato en fechas y documentos.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.10+
*   **Base de Datos:** [SQLite3](https://python.org) (Motor embebido local)
*   **Estilo Visual:** Interfaz CLI interactiva optimizada para una navegación fluida por consola.

---

### 📂 API de la Capa de Negocio (`logica_sistema.py`)

Las reglas del negocio clínico y las mutaciones de datos se gestionan a través de componentes modulares de alta cohesión:

| Componente Lógico | Funcionalidad Core | Impacto Técnico |
| :--- | :--- | :--- |
| **Manejo de Pacientes** | Alta, consulta y edición | Validaciones relacionales mediante consultas parametrizadas para evitar vulnerabilidades de inyección. |
| **Historias Médicas** | Seguimiento y registro de evolución | Estructura de logs relacionales cronológicos enlazados de forma unívoca a la ID del paciente. |
| **Módulo de Turnos** | Asignación y control de agenda | Algoritmos de ordenamiento y control de disponibilidad de tiempo para evitar conflictos de horarios. |

---

### ⚙️ Instalación y Ejecución Local

Sigue estos pasos detallados para desplegar y probar el sistema en tu entorno local utilizando VS Code o tu terminal:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   ```
2. **Navegar al directorio principal:**
   ```bash
   cd gestion-pacientes
   ```
3. **Instalar dependencias necesarias:**
   *(Si el proyecto utiliza librerías adicionales como `colorama`, asegúrate de inicializar tu archivo de dependencias).*
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar el orquestador principal:**
   ```bash
   python app.py
   ```
   *(Nota: El motor SQL creará de forma automática el archivo binario `registro_pacientes.db` en la raíz del proyecto durante el primer inicio).*

---

### 📄 Licencia

Este software se distribuye bajo la Licencia MIT. Libre para modificación, distribución con fines académicos y desarrollo profesional continuo.

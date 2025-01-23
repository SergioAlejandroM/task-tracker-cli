# Task Tracker CLI

**Task Tracker CLI** es una herramienta de línea de comandos que permite gestionar tareas de manera eficiente. Diseñada para simplificar el seguimiento de tus actividades, esta aplicación es ideal para organizar lo que necesitas hacer, lo que ya has completado y en qué estás trabajando actualmente.

---

## 🚀 **Características principales**

- **📌 Agregar tareas:** Registra nuevas tareas con una breve descripción.
- **🔄 Actualizar tareas:** Modifica la descripción de una tarea existente.
- **✅ Marcar tareas:** Cambia el estado de las tareas a "En progreso" o "Realizada".
- **🗑️ Eliminar tareas:** Elimina tareas que ya no son necesarias.
- **📋 Listar tareas:** Visualiza todas las tareas organizadas por estado:
  - Tareas pendientes.
  - Tareas en progreso.
  - Tareas realizadas.

---

## 🛠️ **Requisitos del sistema**

- Lenguaje: **Python 3.8+**
- Módulos estándar: `os`, `json`, `sys`, `datetime`

---

## 🎯 **Propiedades de una tarea**

Cada tarea registrada incluye:

- **ID:** Identificador único.
- **Descripción:** Detalle de la tarea.
- **Estado:** Puede ser `todo`, `in-progress` o `done`.
- **Fecha de creación:** Marca cuándo fue creada la tarea.
- **Última actualización:** Fecha de la última modificación.

---

## 📖 **Guía de uso**

### **Inicialización**
Al ejecutar el programa por primera vez, se crea un archivo `tasks.json` en el directorio actual para almacenar las tareas.

### **Comandos principales**

1. **Agregar una tarea**
   ```bash
   python task_cli.py add "Comprar alimentos"
   ```
   _Salida:_ `Tarea agregada exitosamente (ID: 1)`

2. **Actualizar una tarea**
   ```bash
   python task_cli.py update 1 "Comprar alimentos y cocinar cena"
   ```

3. **Eliminar una tarea**
   ```bash
   python task_cli.py delete 1
   ```

4. **Marcar una tarea como en progreso**
   ```bash
   python task_cli.py mark-in-progress 1
   ```

5. **Marcar una tarea como realizada**
   ```bash
   python task_cli.py mark-done 1
   ```

6. **Listar todas las tareas**
   ```bash
   python task_cli.py list
   ```

7. **Listar tareas por estado**
   - Tareas realizadas:
     ```bash
     python task_cli.py list done
     ```
   - Tareas pendientes:
     ```bash
     python task_cli.py list todo
     ```
   - Tareas en progreso:
     ```bash
     python task_cli.py list in-progress
     ```

---

## 🌟 **Estructura del proyecto**

```plaintext
📂 task-tracker-cli
├── task_cli.py   # Código principal de la aplicación
├── tasks.json    # Archivo JSON para almacenar las tareas
└── README.md     # Documentación del proyecto
```

---

## ⚡ **Mejoras futuras**

- Implementar soporte para subtareas.
- Agregar recordatorios mediante notificaciones.
- Incluir una interfaz gráfica (GUI).

---

## 🖌️ **Vista visual mejorada**

### **Estado de las tareas**

```plaintext
[TODO] Comprar alimentos
[IN-PROGRESS] Cocinar cena
[DONE] Limpiar la casa
```

---

¡Gracias por usar **Task Tracker CLI**! 🎉


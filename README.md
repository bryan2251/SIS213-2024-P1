# Laboratorito - Programacion en pares



### Enunciado

Crear una aplicacion de lista de tareas que permita a los usuarios agregar nuevas tareas, marcarlas como completadas, eliminarlas de la lista, generar reportes por estados de tareas en curso y tareas completadas.

La aplicacion debe ser implementada utilizando un lenguaje de programacion de su eleccion (Python) y debe incluir una interfaz de linea de comandos(CLI) para interactuar con ella (Menú de opciones)

Se usara Programacion Modular

### Analisis del problema

El programa tiene como requerimientos:

* Crear nuevas tareas en una lista
* Marcar el estado de las tareas
* Eliminarlas de la lista si son nuevas
* Generar reportes por estados de tareas en curso y/o tareas completadas

### Diseño solucion

Crearemos diferentes modulos con las funciones necesarias mediante el manejo de listas definiendolas con sus atributos necesarios como son Nombre - Tiempo - Estado 
Ejemplo: 
* Estudiar IS - 15:00 - NUEVO
* Investigar GIT - 19:00 - En curso
* Desarrollar APP - 21:00 - Completado

Despues de desarollar el diseño de lista de tareas se iran agregando funciones como la creacion de nuevas tareas en la lista en base al tiempo, como tambien la posibilidad de cambiar su estado para definirlas como completadas o en curso, ademas de la funcionalidad de eliminar las tareas que se encuentren con un estado de NUEVO, todo esto debe ser manejado unicamente mediante comandos por consola, junto a la interfaz que sera igualemente solo por consola (Menus y Informacion)
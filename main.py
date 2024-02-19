from datetime import datetime
from task_manager import add_task,delete_task

class TodoList:
    def __init__(self):
        """Inicializa la lista de tareas vacía."""
        self.tasks = []

    def complete_task(self, index):
        """Marca una tarea como completada."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "Completado"
        else:
            print("Índice de tarea inválido")

    def mark_as_pending(self, index):
        """Marca una tarea como pendiente."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["status"] = "Pendiente"
        else:
            print("Índice de tarea inválido")

    def generate_report(self):
        """Genera un reporte mostrando todas las tareas."""
        print("Reporte de tareas:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['task']} - {task['time']} - {task['status']}")


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Marcar tarea como pendiente")
        print("4. Eliminar tarea")
        print("5. Generar reporte")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            name = input("Ingrese el nombre de la nueva tarea: ")
            time = input("Ingrese la hora de la nueva tarea: ")
            state = "Nueva"
            add_task(todo_list, name, time, state)
            print("Tarea agregada con éxito.")
        elif choice == "2":
            index = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
            todo_list.complete_task(index)
            print("Tarea marcada como completada.")
        elif choice == "3":
            index = int(input("Ingrese el número de la tarea a marcar como pendiente: ")) - 1
            todo_list.mark_as_pending(index)
            print("Tarea marcada como pendiente.")
        elif choice == "4":
            index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            delete_task(todo_list,index)
            print("Tarea eliminada.")
        elif choice == "5":
            todo_list.generate_report()
        elif choice == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()

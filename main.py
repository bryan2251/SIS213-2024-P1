class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Índice de tarea inválido")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Índice de tarea inválido")

    def generate_report(self):
        pending_tasks = [task["task"] for task in self.tasks if not task["completed"]]
        completed_tasks = [task["task"] for task in self.tasks if task["completed"]]
        print("Tareas pendientes:")
        for task in pending_tasks:
            print("- " + task)
        print("\nTareas completadas:")
        for task in completed_tasks:
            print("- " + task)


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Eliminar tarea")
        print("4. Generar reporte")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            task = input("Ingrese la nueva tarea: ")
            todo_list.add_task(task)
            print("Tarea agregada con éxito.")
        elif choice == "2":
            index = int(input("Ingrese el índice de la tarea a marcar como completada: "))
            todo_list.complete_task(index)
            print("Tarea marcada como completada.")
        elif choice == "3":
            index = int(input("Ingrese el índice de la tarea a eliminar: "))
            todo_list.delete_task(index)
            print("Tarea eliminada.")
        elif choice == "4":
            todo_list.generate_report()
        elif choice == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()

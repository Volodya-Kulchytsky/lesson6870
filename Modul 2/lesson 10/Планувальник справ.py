import datetime

todo_list = []

def save_tasks(todo_list):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in todo_list:
            name = task["name"]
            description = task["description"]
            deadline = task["deadline"]
            priority = task["priority"]
            task0 = f"{name}|{description}|{deadline}|{priority}\n"
            file.write(task0)

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
               space = line.strip().split("|")
               name = space[0]
               description = space[1]
               deadline = datetime.date.fromisoformat(space[2])
               priority = space[3]
               task = {
                    "name": name,
                    "description": description,
                    "deadline": deadline,
                    "priority": priority
               }
               todo_list.append(task)
    except FileNotFoundError:
        pass

def add_task():
    name = input("Введіть назву справи: ")
    description = input("Введіть опис справи (опціонально): ")
    while True:
        try:
            print("Введіть дедлайн справи:")
            year = int(input("Введіть рік дедлайну: "))
            month = int(input("Введіть місяць дедлайну: "))
            day = int(input("Введіть день дедлайну: "))
            deadline = datetime.date(year, month, day)
            break
        except ValueError:
            print("Неправильний формат дати.Спробуйте ще раз")
    priority = input("Введіть пріорітетність вашої справи (високий, середній, низький): ")
    if priority not in ["високий", "середній", "низький"]:
        priority = "середній"

    task = {"name": name,
            "description": description,
            "deadline": deadline,
            "priority": priority}
    todo_list.append(task)
    save_tasks(todo_list)
    print("Справу додано")

def show_todo_list():
    if not todo_list:
        print("Справ немає")
        return
    print("Список справ: ")
    for x, task in enumerate(todo_list, 1):
        print(f"{x}. {task['name']} - {task['deadline']} - {task['priority']}")
        if task["description"]:
            print(f"Опис завдання: {task["description"]}")

def show_today_todo_list():
    load_tasks()
    today = datetime.date.today()
    print("Справи на сьогодні:")
    count = 0
    for x, task in enumerate(todo_list, 1):
        if task['deadline'] == today:
            count += 1
            print(f"{x}, {task['name']} - {task['deadline']} - {task['priority']}")
            if task["description"]:
                print(f"Опис завдання: {task["description"]}")
    if count == 0:
        print("На сьогодні справ немає")

def show_tasks_by_priority():
    priority0 = input("Введіть пріорітетність вашої справи (високий, середній, низький): ")
    if priority0 not in ["високий", "середній", "низький"]:
        print("Невірний пріорітет")
        return
    count0 = 0
    for i, task in enumerate(todo_list, 1):
        if task['priority'] == priority0:
            count0 += 1
            print(f"{i}, {task['name']} - {task['deadline']} - {task['priority']}")
            if task["description"]:
                print(f"Опис завдання: {task['description']}")
    if count0 == 0:
        print("Справ з таким пріорітетом не знайдено")


def delete_task():
    show_todo_list()
    try:
        number = int(input("Введіть номер справи яку хочете видалити: "))
    except ValueError:
        print("Потрібно ввести число")
        return
    if 1 <= number <= len(todo_list):
        todo_list.pop(number - 1)
        print("Справу видалено")
    else:
        print("Справи з таким номером немає, спробуйте ще раз")
    save_tasks(todo_list)

def delete_all_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        pass
    todo_list.clear()
    print("Всі справи видалено")

def menu():
    load_tasks()
    while True:
        menu0 = """        --- Планувальник справ ---
        1.Додати завдання
        2.Видалити завдання
        3.Очистити всі справи
        4.Переглянути список завдань
        5.Переглянути завдання на сьогодні
        6.Переглянути справи за пріоритетом
        7.Вийти
                    """
        print(menu0)
        answer = input("Виберіть опцію: ")
        if answer == "1":
            add_task()
        elif answer == "2":
            delete_task()
        elif answer == "3":
            delete_all_tasks()
        elif answer == "4":
            show_todo_list()
        elif answer == "5":
            show_today_todo_list()
        elif answer == "6":
            show_tasks_by_priority()
        elif answer == "7":
            print("Ви вийшли з програми.")
            break
        else:
            print("Ви не вибрали правильну опцію, спробуйте ще раз.")

print(menu())







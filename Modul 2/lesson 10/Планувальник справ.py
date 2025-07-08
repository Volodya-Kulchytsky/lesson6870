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
    except FileNotFoundError as error:
        pass
        print(error)

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
        except ValueError as error:
            print("Неправильний формат дати.Спробуйте ще раз")
            print(error)
    priority = input("Введіть пріорітетність справи (високий, середній, низький): ")
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
            print(f"Опис завдання: {task['description']}")

def show_today_todo_list():
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
        print("Неправильна пріорітетність")
        return
    count0 = 0
    for x, task in enumerate(todo_list, 1):
        if task['priority'] == priority0:
            count0 += 1
            print(f"{x}, {task['name']} - {task['deadline']} - {task['priority']}")
            if task["description"]:
                print(f"Опис завдання: {task['description']}")
    if count0 == 0:
        print("Справ з таким пріорітетом не знайдено")

def show_tasks_by_date():
    while True:
        try:
            print("Введіть дедлайн справи:")
            year = int(input("Введіть рік дедлайну: "))
            month = int(input("Введіть місяць дедлайну: "))
            day = int(input("Введіть день дедлайну: "))
            deadline0 = datetime.date(year, month, day)
            break
        except ValueError as error:
            print("Неправильний формат дати.Спробуйте ще раз")
            print(error)
    count1 = 0
    for x, task in enumerate(todo_list, 1):
        if task['deadline'] == deadline0:
            count1 += 1
            print(f"{x}. {task['name']} - {task['deadline']} - {task['priority']}")
            if task["description"]:
                print(f"Опис завдання: {task['description']}")
    if count1 == 0:
        print("Справ на цю дату немає")

def delete_task():
    show_todo_list()
    try:
        number = int(input("Введіть номер справи яку хочете видалити: "))
    except ValueError as error:
        print("Потрібно ввести число")
        print(error)
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

def edit_tasks():
    show_todo_list()
    try:
        number = int(input("Введіть номер справи яку хочете редагувати: "))
    except ValueError as error:
        print("Потрібно ввести число")
        print(error)
        return
    if 1 <= number <= len(todo_list):
        task = todo_list[number - 1]
    print("Щоб пропустити редагування просто нажміть Enter")
    new_name = input(f"Введіть нову назву ({task['name']}): ")
    if new_name:
        task["name"] = new_name
    new_description = input(f"Введіть новий опис ({task['description']}): ")
    if new_description:
        task["description"] = new_description
    new_deadline = input("Хочете змінити дедлайн? (так/ні): ")
    if new_deadline == "так":
        while True:
            try:
                new_year = int(input("Введіть новий рік: "))
                new_month = int(input("Введіть новий місяць: "))
                new_day = int(input("Введіть новий день: "))
                task["deadline"] = datetime.date(new_year, new_month, new_day)
                break
            except ValueError:
                print("Неправильний формат дати.Спробуйте ще раз")
    new_priority = input(f"Введіть нову пріорітетність ({task['priority']}): ")
    if new_priority in ["високий", "середній", "низький"]:
        task["priority"] = new_priority
    save_tasks(todo_list)
    print("Справу редаговано")

def menu():
    load_tasks()
    while True:
        menu0 = """        --- Планувальник справ ---
        1.Додати справy
        2.Видалити справу
        3.Очистити всі справи
        4.Переглянути список справ
        5.Переглянути справи на сьогодні
        6.Переглянути справи за пріоритетом
        7.Переглянути справи за датою
        8.Редагувати справи
        9.Вийти
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
            show_tasks_by_date()
        elif answer == "8":
            edit_tasks()
        elif answer == "9":
            print("Ви вийшли з програми.")
            break
        else:
            print("Ви не вибрали правильну опцію, спробуйте ще раз.")

print(menu())







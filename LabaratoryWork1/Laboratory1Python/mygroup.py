groupmates = [
    {
        "name": "Агарков",
        "surname": "Максим",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },

    {
        "name": "Смирнов",
        "surname": "Феликс",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },

    {
        "name": "Шацкий",
        "surname": "Егор",
        "exams": ["Философия", "ИС", "МЛИТА"],
        "marks": [5, 5, 4]
    },

    {
        "name": "Соцков",
        "surname": "Игнатий",
        "exams": ["Социология", "АГИЛА", "ВМ"],
        "marks": [4, 5, 4]
    },

    {
        "name": "Копытько",
        "surname": "Сергей",
        "exams": ["СТ", "СП", "ФизРа"],
        "marks": [5, 5, 5]
    },

    {
        "name": "Крутиков",
        "surname": "Степан",
        "exams": ["ЭДО", "ДМ", "АВС"],
        "marks": [4, 3, 3]
    }

]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))

    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))

    print("Введите срдений балл: ")
    avgMark = input()
    print("Список студентов с указанным средним баллом")
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20), u"Средний Балл".ljust(5))

    for student in students:
        avg = round(sum(student["marks"]) / len(student["marks"]))
        if str(avgMark) == str(avg):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
                  str(student["marks"]).ljust(20), str(avg).ljust(5))


print_students(groupmates)

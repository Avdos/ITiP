groupmates = [
    {
        "name": "Доменик",
        "surname": "Торетто",
        "exams": ["Моделирование", "ИТП", "БЖ"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Брайн",
        "surname": "Оконнер",
        "exams": ["Метрология", "РОС", "БЖ"],
        "marks": [4, 5, 3]
    },
    {
        "name": "Летти",
        "surname": "Ортис",
        "exams": ["Философия", "ИС", "БЖ"],
        "marks": [5, 3, 3]
    },
    {
        "name": "Тедж",
        "surname": "Паркер",
        "exams": ["Электропитание", "АИС", "БЖ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Роман",
        "surname": "Пирс",
        "exams": ["Маркетинг", "ЭБЖ", "БЖ"],
        "marks": [5, 5, 3]
    }
]
def mean(students):
    x = int(input("Введите средний балл\n"))
    for student in students:
        mean_marks = sum(student['marks'])/len(student['marks'])
        if mean_marks > x:
            print(student["name"].ljust(15), student["surname"].ljust(10))

mean(groupmates)
            

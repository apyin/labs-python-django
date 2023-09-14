groupmates = [					
    {
        "name": "Иван",
        "surname": "Коледов",
        "exams": ["ИТиП", "РОС", "УиАвИС"],
        "marks": [3, 3, 5]
    },

    {
        "name": "Александр",
        "surname": "Каргашинский",
        "exams": ["ИТиП", "РОС", "УиАвИС"],
        "marks": [4, 3, 5]
    },

    {
        "name": "Полина",
        "surname": "Тюрина",
        "exams": ["АрхИС", "МиСПИСиТ", "ОС"],
        "marks": [4, 5, 3]
    },

    {
        "name": "Павел",
        "surname": "Пиляк",
        "exams": ["АрхИС", "МиСПИСиТ", "ОС"],
        "marks": [4, 4, 3]
    },

    {
        "name": "Константин",
        "surname": "Пономаревский",
        "exams": ["АрхИС", "МиСПИСиТ", "ОС"],
        "marks": [2, 3, 4]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


def average_mark(students):
	print("Input a mean value: ")
	mean_val = float(input())
	print(u"Имя".ljust(15), u"Фамилия".ljust(20), u"Экзамены".ljust(30), u"Оценки".ljust(20))
	for st in students:
		mean = (st["marks"][0]+st["marks"][1]+st["marks"][2])/3
		if mean > mean_val:
			 print(st["name"].ljust(15), st["surname"].ljust(10), str(st["exams"]).ljust(30), str(st["marks"]).ljust(20))
			
#print_students(groupmates)
average_mark(groupmates)
#print(groupmates[0]["marks"][0])
#print((groupmates[0]["marks"][0]+groupmates[0]["marks"][1]+groupmates[0]["marks"][2])/3)

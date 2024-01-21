# Exercise 7: Find youngest student
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student

def finde_youngest_stud(students_info):
    min = students_info["student1"]['age']
    kluch = 0
    for k,v in students_info.items():
        if min > v["age"]:
            min = v["age"]
            kluch = k
    return students_info[kluch]        


print(finde_youngest_stud({
    'student1': {
        'name': 'John Doe',
        'age': 20,
        'subjects': ['Math', 'Physics', 'English'],
        'scores': [7, 9, 9, 6]
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 19,
        'subjects': ['Chemistry', 'Biology', 'History'],
        'scores': [5, 6, 8, 10]
    },
    'student3': {
        'name': 'Bob Johnson',
        'age': 21,
        'subjects': ['Computer Science', 'Statistics', 'Psychology'],
        'scores': [8, 8, 9, 9, 9]
    }
}))
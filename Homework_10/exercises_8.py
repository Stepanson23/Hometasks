# Exercise 8: Find student with highest average score
# Write a function that takes a dictionary with information about students. Return info
# about the youngest student

def tvab_mij(number):
    sum = 0
    for i in number:
        sum += i
    return sum/len(number)

def finde_youngest_stud(students_info):
    kluch = 0
    mij = tvab_mij(students_info["student1"]["scores"])
    for k in students_info.keys():
        compare = tvab_mij(students_info[k]["scores"])
        if mij < compare:
            mij = compare
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
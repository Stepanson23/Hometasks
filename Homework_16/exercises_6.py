# 6. Tuple Exercise:
# Create a tuple of student names and their corresponding scores. Write a function to find
# the student with the highest score.


def high_score(students):
    max_score = 0
    for i in students:
        if i[1] > max_score:
            max_score = i[1]
    return max_score        


print(high_score((
    ("Alica", 95),
    ("Bob", 60),
    ("Charli", 22),
    ("David", 45),
    ("Eva", 84),
    ("Frank", 61),
    ("Grno", 76)
)))
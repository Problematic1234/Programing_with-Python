# DATE = 27 OCTOBER 2022

marks = [95, 98, 97]
marks.insert(0, 99)
print(marks)

marks = [95, 98, 97, 89]
marks.insert(0, 99)
print(99 in marks)

marks = [95, 98, 97, 90]
print(len(marks))

marks = [95, 98, 97]
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

marks = [95, 89, 99]
marks.clear()
print(marks)

# BREAK AND CONTINUE
students = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in students:
    if student == "radha":
        break
    print(student)

students = ["RAM", "SHYAM", "KISHAN", "RADHA", "RADHIKA"]
for student in students:
    if student == "kishan":
        continue
    print(student)

# TUPLE
marks = (95, 98, 97, 97, 97)
print(marks.count(97))

marks = (95, 98, 97, 97, 97)
print(marks.index(97))

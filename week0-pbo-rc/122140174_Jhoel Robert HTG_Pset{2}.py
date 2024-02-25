# For the next Problem set, You’re going to insert a student’s grade score into a dictionary. So given a integer as the number of students. Use the for loop to insert the student’s data name and grade. So at the end you would have a dictionary like this

dict_grade = {}

num_items = int(input("Banyaknya Data yang ingin di Input: "))

for i in range(num_items):
    name = input("Nama: ")
    grade = input("Nilai: ")
    dict_grade[name] = grade

print(f"Grade = ", dict_grade)
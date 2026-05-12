file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("pralad, 1001\n")
file.write("Karma, 1002\n")
file.write("arjun, 1003\n")
file.write("Tashi, 1004\n")
file.write("dorji, 1005\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
search = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if search.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()

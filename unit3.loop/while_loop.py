no_of_students = int(input("enter the number of the student: "))
i = 1 #initalization
student_name  = {} #empty dictionary to store the names of the students་.
while i <= no_of_students:#condition
    name = input("enter the name of the student: ")
    print("the name of the student{} is {}". format(i,name))
    i += 1 #incrementing the value of i by 1 each iteration of the loop
    student_name[1] = name #it adds the name of the student to the dictionary student_names with the key as the value of i.

print(student_name) #it prints the dictionary student_names which contains the naems of the students enterded by the user.

while True:
    print("this is an infinite loop.press ctrl + c to stop it .")

Marks1 = float(input("Enter the marks of the first subject:"))
Marks2 = float(input("Enter the marks of the second subject:"))
Marks3 = float(input("Enter the marks of third third subject:"))
average = ( Marks1 + Marks2 + Marks3)/ 3
print("the average of 3 subjests are %.2f " %average )

if(average >= 90 and Marks1 >= 50 and Marks2 >= 50 and Marsk3 >= 50): 
    print("Grade: A")
elif(average >= 80 and Marks1 >= 50 and Marks2 >= 50 and Marks3 >= 50):
    print("Grade: B")
elif(average >= 70 and Marks1 >= 50 and Marks2 >= 50 and Marks3 >= 50):
    print("Grade: C")
elif(average >= 60 and Marks1 >= 50 and Marks2 >= 50 and Marks3 >= 50):
    print("Grade: D")
elif(average >= 60 and Marks1 >= 50 and Marls2 >= 50 and Marks3 >= 50):
    print("Grade: E")
else:
    print("you need to work harder.")
for i in range(1,4): #outer loop iterates from 1 tp 3
    for j in range(i): #inner loop iterates from 0 to i-1
     print(f"outer loop iteration {i} , inner loop iteration {j+1}")

for i in range(4): #it represents the number of rows of stars to be printed. it iterates from 0 to 3, which means it will print 4 rows of stars.
    for j in range(i): #it represents the number of stars to be printed in each row.
        print("*" , end = " ") #end parameter is used to specify what to print at the end of the output. By default, it is a new line character but here we are using space to print the stars in the same line.
    print() #print a newline charater after each rows of stars.

#activity
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

for i in range(6,0,-1):
    for j in range(i):
        print("*" , end = " ")
    print()
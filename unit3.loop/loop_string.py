name = input("enter your name:")
for i in name:
    print(i)

li = ["python programing","python fundamentals","python interview questions"]
for x in li: # x is a variable that takes the value of each item in the list li during each iteration of the loop.
    print(x)

lenli = len(li) # len() returns the number of items in the list li i.e.3. this value isstored in the variable lenli.
for x in range(lenli): #x is a variable that takes the value of each index.
    print(li[x])

tupleli = tuple(li)
for x in range (len(tupleli)): 
    print(tupleli[x])

setli = set(li)
for x in setli:
    print (x)
    
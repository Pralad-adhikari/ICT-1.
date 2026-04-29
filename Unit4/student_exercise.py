def fun1(x, y):
    if x == 0:
        return y
    else:
        return fun1(x - 1, y + x)

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

result = fun1(x, y)

print("output:", result)

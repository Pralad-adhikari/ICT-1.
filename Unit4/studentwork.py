def pattern(n):
    if n == 1:
        print("*")
    else:
        pattern(n - 1)   # recursive call
        print("* " * n)  # print after recursion


# Taking input from user
n = int(input("Enter value of n: "))
pattern(n)
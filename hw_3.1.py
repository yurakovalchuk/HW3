n_1 = int(input("Type first number: "))
n_2 = int(input("Type second number: "))
action = input("Type action: '*', '-', '+', '/' ")

if action == "*":
    print(n_1 * n_2)
elif action == "-":
    print(n_1 - n_2)
elif action == "+":
    print(n_1 + n_2)
elif action == "/":
    if n_1 == 0 or n_2 == 0:
        print("One number is equal to zero")
    else:
        print(n_1 / n_2)
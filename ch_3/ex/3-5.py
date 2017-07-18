print("Calculator")

num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

print("(1) + \n(2) - \n(3) * \n(4) /")

sel = int(input("Please select something (1-4): "))

if sel == 1:
    print("The result is: ",num1 + num2)
elif sel == 2:
    print("The result is: ", num1 - num2)
elif sel == 3:
    print("The result is: ", num1 * num2)
elif sel == 4:
    print("The result is: ", num1 / num2)
else:
    print("Selection was not correct.")



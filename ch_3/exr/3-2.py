name = input("Give name: ")

if name == "John":
    pwd = input("Give password: ")
    if pwd == "ABC123":
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")

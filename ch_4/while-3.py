# for i in range(0, 5):
#     print(i)

keep_going = True

while keep_going:
    u_input = input("Write something: ")

    if u_input == "End":
        keep_going = False
    else:
        print(u_input)

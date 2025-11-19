command  = int(input("Enter the size of the pattern: "))

row = 0
while row < command:

    for _ in range(command):
        print("*", end="")

    print()

    row += 1
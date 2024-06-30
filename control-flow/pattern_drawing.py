size = int(input("Enter the size of the pattern: "))

i = 0

while i < size:
    i += 1

    j = 0
    for j in range(size):
        j += 1
        print("*" ,end="")
    print()
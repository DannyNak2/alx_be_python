# Define a variable that prompt user to enter a size
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side for each column in the row
    for col in range(size):
        print("*", end="")
    # Print a newline character after completing each row
    print()
    # Increment the row counter
    row += 1

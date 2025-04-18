# Problem-2: Generate first 'a' odd numbers starting from 1

# Input from the user
try:
    a = int(input("Enter a number: "))

    if a <= 0:
        print("Please enter a positive number.")
    else:
        # Print first 'a' odd numbers
        for i in range(a):
            print(2 * i + 1, end=", " if i < a - 1 else "\n")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

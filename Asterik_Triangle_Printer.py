def print_tri():
    print("Hello. This script prints out a triangle based on asterik symbol multiplied times your number./n")
    print("Please type a number below to print out a triangle. Remember to not enter a number too large, otherwise the triangle might not fit your screen and may look unusal.")
    while True:
        num = input("\nEnter a number: ")

        try:
            num = int(num)
            if num <= 0:
                print("Please enter a number greater than 0.")
                continue

            count = 1
            while count != num + 1:
                print("*" * count)
                count += 1
            exit()

        except ValueError:
            print("Invalid input. Please try again.")
            print_tri()

print_tri()
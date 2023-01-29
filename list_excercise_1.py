list_of_numbers = [18, 12, 99, 82, 29, 89, 25, 60, 28, 74, 38, 31, 14, 16, 62, 26, 90, 56, 58, 43, 47, 39, 51, 8, 80, 52, 63, 57, 45, 97, 72, 48, 19, 41, 85, 92, 69, 54, 3, 93, 78, 64, 79, 6, 59, 55, 11, 68, 1, 34, 33, 36, 32, 10, 76, 61, 96, 23, 66, 44, 30, 91, 95, 27, 94, 40, 65, 73, 53, 46, 67, 2, 0, 37, 81, 9, 70, 15, 77, 98, 49, 24, 83, 86, 84, 75, 20, 35, 42, 71, 4, 21, 87, 13, 88, 5, 17, 50, 22, 7]

# Task is to print all even numbers

# create a "for loop"
for number in list_of_numbers:
    # find the remainder of the number
    remainder = number % 2

    # if remainer is equals to 0, it is a even number so print the number else do nothing.
    if remainder == 0:
        print(f"{number} is EVEN.")
    else:
        print(f"{number} is ODD.")

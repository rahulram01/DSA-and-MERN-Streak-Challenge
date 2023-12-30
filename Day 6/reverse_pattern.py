def print_number_triangle(last_number):
    for row in range(1, last_number + 1):
        for column in range(row, 0, -1):
            print(column, end='')
        print("")


last_number = int(input("Enter the last number: "))


print_number_triangle(last_number)

def print_star_pattern(n):
    first_half = (n + 1) // 2
    second_half = n // 2

    # First Half
    curr_row = 1 
    while curr_row <= first_half:
        spaces = 1 
        while spaces <= (first_half - curr_row):
            print(" ", end="")
            spaces += 1
        curr_col = 1
        while curr_col <= (2 * curr_row) - 1:
            print("*", end="")
            curr_col += 1
        print()
        curr_row += 1

    # Second Half 
    curr_row = second_half 
    while curr_row >= 1:
        spaces = 1
        while spaces <= (second_half - curr_row + 1):
            print(" ", end="") 
            spaces += 1
        curr_col = 1 
        while curr_col <= (2 * curr_row) - 1:
            print("*", end="") 
            curr_col += 1
        print()
        curr_row -= 1

# Get user input for n
n = int(input("Enter the value of n: "))

# Call the function with the user input
print_star_pattern(n)

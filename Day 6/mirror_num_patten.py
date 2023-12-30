def print_number_triangle_with_spaces(n):
    for x in range(1, n + 1):
        for y in range(n, x, -1):
            print(" ", end="")
        for z in range(1, x + 1):
            print(z, end="")
        print("")


n = int(input("Enter the value of n: "))


print_number_triangle_with_spaces(n)


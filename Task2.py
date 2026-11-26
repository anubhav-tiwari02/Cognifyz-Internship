
def right_triangle(rows):
    print("\nRight-Angled Triangle:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def inverted_triangle(rows):
    print("\nInverted Triangle:")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def pyramid(rows):
    print("\nNumber Pyramid:")
    for i in range(1, rows + 1):
        print("  " * (rows - i), end="")

        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        print()


print("================================")
print("      NUMBER PATTERN GENERATOR")
print("================================")

try:
    rows = int(input("Enter the number of rows (1-20): "))

    if 1 <= rows <= 20:
        right_triangle(rows)
        inverted_triangle(rows)
        pyramid(rows)
    else:
        print("Please enter a number between 1 and 20.")

except ValueError:
    print("Invalid input! Please enter an integer.")

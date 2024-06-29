def print_honeycomb(rows, columns):
    if rows <= 0 or columns <= 0:
        print("Row and colum are positive")
        return

    for row in range(rows):
        if row % 2 == 1:
            print("  ", end="")

        #  top
        for col in range(columns):
            print("  _   ", end="")
        print()

        #  upper middle
        if row % 2 == 1:
            print("  ", end="")
        for col in range(columns):
            print(" / \\ ", end="")
        print()

        #  lower middle
        if row % 2 == 1:
            print("  ", end="")
        for col in range(columns):
            print(" \\_/ ", end="")
        print()


# Example
rows = 3
columns = 5
print_honeycomb(rows, columns)
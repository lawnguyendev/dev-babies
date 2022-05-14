def main():
    # week2_ex1()

    s = sum(1, 2)
    print(s)


# supported function
def sum(no_1, no_2):
    sum = no_1 + no_2
    return sum

# tinh tong 2 so


def week2_ex1():
    print("===SUM===")
    num_1 = input("Number 1: ")
    num_2 = input("Number 2: ")
    sum = num_1 + num_2

    print(f"Sum of {num_1} and {num_2} is: {sum}")


main()

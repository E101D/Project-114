a = 25


def integer():
    if b > a:
        print("b is greater than a")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

while True:
    b = int(input("Enter a number here: "))

    integer()

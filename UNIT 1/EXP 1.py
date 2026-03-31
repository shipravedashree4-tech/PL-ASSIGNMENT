# FINAL COMBINED PROGRAM

def show_family():
    myfamily = {
        "child1": {"name": "Emil", "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
        "child3": {"name": "Linus", "year": 2011}
    }
    for key, value in myfamily.items():
        print(f"{key}: Name = {value['name']}, Year = {value['year']}")


def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n - 1)


def calculate_factorial():
    num = int(input())
    print(factorial(num))


def check_prime():
    num = int(input())
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")


def fibonacci():
    n = int(input())
    num1, num2 = 0, 1
    count = 1
    while count <= n:
        print(num2, end=" ")
        num1, num2 = num2, num1 + num2
        count += 1
    print()


while True:
    print("1.Dictionary 2.Factorial 3.Prime 4.Fibonacci 5.Exit")
    choice = input()
    if choice == '1':
        show_family()
    elif choice == '2':
        calculate_factorial()
    elif choice == '3':
        check_prime()
    elif choice == '4':
        fibonacci()
    elif choice == '5':
        break
    else:
        print("Invalid")
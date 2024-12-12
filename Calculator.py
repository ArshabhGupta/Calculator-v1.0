def add(a, b):
    sum = a + b
    return sum

def subtract(a, b):
    sum = a - b
    return sum

def multiply(a, b):
    sum = a * b
    return sum

def divide(a, b):
    sum = a / b
    return sum

def exponent(a, b):
    sum = a ** b
    return sum

def root(a, b):
    sum = a ^ -b
    return sum

def factorial(a):
    for i in range(1, a + 1):
        a = a * i
    return a

def lcm(largest, smallest):
    l1 = largest
    s1 = smallest

    while(smallest):
        store = smallest
        smallest = largest % smallest
        largest = store

    lcm = (s1 * l1) / largest
    return lcm

def hcf(largest, smallest):

    largest = int(input("Enter the larger number: "))
    smallest = int(input("Enter the smaller number: "))

    while(smallest):
        store = smallest
        smallest = largest % smallest
        largest = store

    return largest

print("Welcome to the calculator!")

while True:
    print("Choose your operation:-")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponention")
    print("6. Roots")
    print("7. Factorial")
    print("8. HCF")
    print("9. LCM")

    choice = int(input("Please enter the option number: "))
    
    if choice == 1:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(add(a, b))
    elif choice == 2:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))    
        print(subtract(a, b))
    elif choice == 3:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))    
        print(multiply(a, b))
    elif choice == 4:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))        
        print(divide(a, b))
    elif choice == 5:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(exponent(a, b))  
    elif choice == 6:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(root(a, b))
    elif choice == 7:
        a = int(input("Enter a number: "))
        print(factorial(a))
    elif choice == 8:
        largest = int(input("Enter the larger number: "))
        smallest = int(input("Enter the smaller number: "))
        print(lcm(largest, smallest))
    elif choice == 9:
        largest = int(input("Enter the larger number: "))
        smallest = int(input("Enter the smaller number: "))
        print(hcf(largest, smallest))
    else:
        print("Invalid choice!")

    x = input("Do you want to retry? (Y/N): ")
    if x == 'Y':
        continue
    else:
        break
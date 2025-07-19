def right_triangle(n):
    for i in range(1, n+1):
        print("*" * i)

def pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))

def left_triangle(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * i)

def analyze_range(start, end):
    total = 0
    for num in range(start, end+1):
        print(f"Number {num} is {'Even' if num%2==0 else 'Odd'}")
        total += num
    print(f"Sum of all numbers from {start} to {end} is: {total}")

while True:
    print("\n1. Right-angled Triangle\n2. Pyramid\n3. Left-angled Triangle\n4. Analyze a Range\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter rows: "))
        if n > 0:
            right_triangle(n)
    elif choice == '2':
        n = int(input("Enter rows: "))
        if n > 0:
            pyramid(n)
    elif choice == '3':
        n = int(input("Enter rows: "))
        if n > 0:
            left_triangle(n)
    elif choice == '4':
        start = int(input("Start of range: "))
        end = int(input("End of range: "))
        if start <= end:
            analyze_range(start, end)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

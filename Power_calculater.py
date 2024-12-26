while True:
    print("\nPower calculater")

    num = float(input("Enter the number that you want to multiply "))
    n = int(input("Enter how many times do you want to multiply "))

    num2 = 1
    for i in range(0, n):
        num2 = num2*num

    print("Result= ", num2)
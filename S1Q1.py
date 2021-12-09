 # Factorial digit sum
number = int(input("Enter the Number : "))

factorial =1

if number < 0:
    print("Cant Computer factorial for Negative Numbers")
elif number < 2:
    print("{}! = {}".format(number, factorial))
else:
    for num in range(number, 1, -1):
        factorial = factorial * num

    print("{}! = {}".format(number, factorial))


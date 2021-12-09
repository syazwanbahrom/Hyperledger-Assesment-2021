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

#Find the sum of the digits in the number 100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
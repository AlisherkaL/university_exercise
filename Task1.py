x = int(input("Введите число от 0 до 1000: "))
a = 0

if x < 2:
    print ("Ваше число - не простое и не составное")

else:
    for index in range(2, x):
        if (x % index == 0):
            a = a+1
    if (a < 1):
        print("Ваше число - простое")
    else:
        print("Ваше число - составное")

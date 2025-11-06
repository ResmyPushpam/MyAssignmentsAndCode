number = int(input("Please Enter the number"))
is_prime = True

if  number > 1:
    for divisor in range(2,number):
        if (number % divisor) == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is prime")    
else:
    print("Number is not Prime")
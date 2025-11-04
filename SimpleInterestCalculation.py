Principal = 1000  # Initial amount
Rate = 5         # Annual interest rate in percentage
Time = 3         # Time in years
Simple_Interest = (Principal * Rate * Time) / 100
print(f"The simple interest for a principal of {Principal} at a rate of {Rate}% over {Time} years is:{Simple_Interest} {Simple_Interest}")  
if Simple_Interest > 200:
    print("The simple interest is above 200")   
else:
    print("The simple interest is 200 or below")
    print(f"The simple interest is: {Simple_Interest}") 
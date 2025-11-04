try:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    squared_numbers =[]
    for num in numbers:
        squared_numbers.append(num**2)
    print("Squared Numbers:", squared_numbers)
except Exception as e:
    print("An error occurred:", e)
    


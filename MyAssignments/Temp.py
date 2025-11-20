'''Given an array of temperatures in Celsius [15, 22, 18, 30, 12], write a program that converts 
each temperature to Fahrenheit using the formula: F = (C × 9/5) + 32. Store the results in a new 
array. '''
temp_celsius = [15,22,18,30,12]
temp_Fahrenheit = []
for temp in temp_celsius:
    temp_Fahrenheit.append((temp * 9/5) + 32)
print(temp_Fahrenheit)


Temperature_Celsius = 25
Temperature_Fahrenheit = (Temperature_Celsius * 9/5) + 32
print(f"{Temperature_Celsius}°C is equal to {Temperature_Fahrenheit}°F")
if Temperature_Fahrenheit > 98.6:
    print("The temperature is above normal body temperature.")
else:
    print("The temperature is at or below normal body temperature.")


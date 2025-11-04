Weight = 70  # in kilograms
Height = 1.75  # in meters
BMI = Weight / (Height ** 2)
print(f"Your BMI is: {BMI:.2f}")
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")                   
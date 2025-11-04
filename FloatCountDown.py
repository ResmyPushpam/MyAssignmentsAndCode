FloatNumber = 5.0
float_list = []                     # <-- the list that will hold the values

while FloatNumber > 0:
    float_list.append(FloatNumber)  # <-- store it in the list
    FloatNumber -= 0.5

# After the loop you have the full list:
print("\nCollected numbers:", float_list)
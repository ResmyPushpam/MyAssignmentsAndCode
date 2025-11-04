word = "hello123"
digit_count = 0

for char in word: 
    if char.isdigit():        # ← Added parentheses ()
        digit_count += 1

print(f"The string contains {digit_count} digits.")
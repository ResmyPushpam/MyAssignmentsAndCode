Word="hello"
vowel_count = 0
for char in Word.lower():
    if char in 'aeiou':
        vowel_count += 1
print("Number of vowels:", vowel_count)
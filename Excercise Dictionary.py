Sentence = "the quick brown fox jumps over the lazy dog"
word_count = {}
print(type(word_count))  # Output: <class 'dict'>

for word in Sentence.split():
    word = word.strip(",.!?").lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# Output: {'hello': 1, 'world': 1}

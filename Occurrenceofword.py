Sentence = "the quick brown fox jumps over the lazy dog. the dog barked."
WordToFind = "the"
    count = Sentence.Lower().Split(" ").Count(word.Lower() == WordToFind.Lower())
print(f"The word '{WordToFind}' occurs {count} times in the sentence.")
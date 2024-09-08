def reverse_word():
    word = input("Please enter a word\n")
    actual_word = []
    for word in reversed(word):
        actual_word.append(word)
    s = ""
    print(s.join(actual_word))

reverse_word()
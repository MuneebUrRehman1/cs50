word = input("camelCase: ")
for w in word:
    if w.isupper():
        word = word.replace(w, "_" + w.lower())
print(word)


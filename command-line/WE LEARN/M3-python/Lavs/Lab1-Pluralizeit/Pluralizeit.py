
num = int(raw_input("Enter a number:"))
word = str(raw_input("Enter a word:"))


if num > 1 and word[:-3] == "ife":
    print(word[:-3] + "ives")
elif num > 1 and word[:-2] == "sh":
    print(word[:-2] + "es")
elif num > 1 and word[:-2] == "ch":
    print(word[:-2] + "es")
elif num > 1 and word[:-2] == "us":
    print(word[:-2] + "i")
elif num > 1 and word[:-1] == "y":
    print(word[:-1] + "s")
else:
    print(word + 's')

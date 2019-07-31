# students = ["Alice", "Javi", "Damien"]
# students.append("Delilah")
#     print(students)
#
# students = ["ALice", "Javi", "Damien"]
# students.insert(1, "Zoe")
#     print(students)
#
# students = ["Alice", "Javi", "Damien", "Javi"]
# #students.insert(1, "Zoey")
# students.remove("Javi")
#     print(students)

# smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
# for index in range(len(smith_siblings)):
# for names in smith_siblings:
# smith_siblings[index] = smith_siblings[index] + "smith"
#     print(name + " Smith")
# #
# print(len(smith_siblings))

# superheroes = ["Captain Marvel", "Wonder Woman", "kamala Khan", "Bumblebee", "Jessica Jones"]
# demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5?"))
#
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top % heroes:", superheroes)
# else:
#     print("Hero not found.")

names = ["Rickson", "Bran", "Sansa", "Jon", "Robb"]
# names[::-1]
# print(names[::-1])
# names[4:2:-1]
print(names[::2])



states = {"NY": "New York", "CA": "California", "TX": "Texas"}

states = {
"NY": "New York",
"CA": "California",
"TX": "Texas",
}


for abbreviation in states:
    print(abbreviation + "is short for" + states[abbreviation])

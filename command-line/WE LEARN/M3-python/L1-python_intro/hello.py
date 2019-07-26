"""num2 = int(raw_input("Enter number #2:"))
total = num1 + num2
 print("The sum is"+ str(total))

num = int(raw_input("Enter a number:"))
if num > 0:
 print("Thats's a positive number !")
elif num < 0:
 print("That's a negative number!")
else:
 print("Zero is neither negative or positive")
 """


"""string = "hello there"
for letter in string:
 print(letter.upper())
for i in range(5):
 print(i)

x = 1
while x <= 5:
 print(x)
 x = x + 1

my_name = "Bob"
friend1 = "Alice"
friend2 = "John"
friend3 = "Mallory"
print(
"My name is % and my friends are %, %, and % " %
(my_name, friend1, friend2, and friend3)
)"""

def greetAgent():
     print("Bond. James Bond.")


def createAgentGreeting(first_name, last_name):
     return "%s %s %s." % (last_name, first_name, last_name)


def findsum(x):
    sum = 0
    for i in range (x):
        sum = sum + i
    print(sum)

findsum(11)

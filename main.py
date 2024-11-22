name1 = list(input("Enter your name: ").lower())
name2 = list(input("Enter your crush's name: ").lower())

for element in name1:
    if element == " ":
        name1.pop(name1.index(" "))
for element in name2:
    if element == " ":
        name2.pop(name2.index(" "))

common_letters = set(name1).intersection(set(name2))
print(common_letters)



print(name1,name2)
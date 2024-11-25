name1 = list(input("Enter your name: ").lower())
name2 = list(input("Enter your crush's name: ").lower())

name1 = [char for char in name1 if char != " "]
name2 = [char for char in name2 if char != " "]

common_letters = set(name1).intersection(set(name2))
print(common_letters)

for char in common_letters:
    # Remove all occurrences of the character in name1
    name1 = [c for c in name1 if c != char]
    # Remove all occurrences of the character in name2
    name2 = [c for c in name2 if c != char]



print(name1,name2)
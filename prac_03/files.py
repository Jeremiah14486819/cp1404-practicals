# Writing to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Reading from a file
with open('name.txt', 'r') as file:
    name = file.read()
print(f"Hi {name}!")

# Handling numbers from a file
with open('numbers.txt', 'r') as file:
    total = sum(int(line) for line in file)
print(f"Total: {total}")

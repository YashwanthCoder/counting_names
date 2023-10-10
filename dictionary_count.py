name_count = {}

while True:
    name = input("Enter a name (type 'done' to finish): ")
    if name == 'done':
        break
    name_count[name] = name_count.get(name, 0) + 1

# Print the results in the desired format
for name, count in name_count.items():
    print(f"{name}:{count}")

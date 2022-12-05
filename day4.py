
with open('day4.in') as file:
    data = [i for i in file.read().strip().split("\n")]


# === PART 1 ===
pairs = 0
for entry in data:
    first, second = entry.split(",")
    first = first.split("-")
    second = second.split("-")

    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        pairs += 1
    elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
        pairs += 1

print("Answer to part 1:", pairs)

# === PART 2 ===
pairs = 0
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] in range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        pairs += 1
    elif second[0] in range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        pairs += 1


print("Answer to part 2:", pairs)
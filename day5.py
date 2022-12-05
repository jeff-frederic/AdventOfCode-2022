from string import ascii_uppercase

with open('day5.in') as file:
    stack_strings, instructions = (i.split('\n') for i in file.read().strip('\n').split('\n\n'))


# Initializing a dictionary where we will put all of our chars (crates)
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ","")}

# Helper function to view what's inside the stacks
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

def displayStackInput():
    for stack in stack_strings:
        print(stack)

# Indexes in which the chars (crates) will be found
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]

# Adding the crates to the appropriate stack
for string in stack_strings[:-1]:
    stack_num = 1
    for index in indexes:
        if string[index] == " ":
            pass
        else:
            stacks[stack_num].insert(0, string[index])
        stack_num += 1


# === PART 1 ===
# for instruction in instructions:
#     instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
#     instruction = [int(i) for i in instruction]

#     crates = instruction[0]
#     from_stack = instruction[1]
#     to_stack = instruction[2]

#     for crate in range(crates):
#         crate_removed = stacks[from_stack].pop()
#         stacks[to_stack].append(crate_removed)

# answer = ""
# for stack in stacks:
#     answer += stacks[stack][-1]


# === PART 2 ===
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    crates_to_remove = stacks[from_stack][-crates:]
    stacks[from_stack] = stacks[from_stack][:-crates]
    stacks[to_stack].append(crates_to_remove)
    print(instruction, crates_to_remove)



displayStacks()


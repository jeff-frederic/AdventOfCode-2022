
with open("day7.in") as file:
    commands = file.readlines()

dirs = {"/home":0}
path = "/home"

# Process every command
for command in commands:

    # Commands that start with $
    if command[0] == "$":
        
        # Do nothing 
        if command[2:4] == "ls":
            pass
        
        # Manage changing the path 
        elif command[2:4] == "cd":
            
            # # Go back to the root
            if command[5:6] == "/":
                path = "/home"

            # Go back in the path
            elif command[5:7] == "..":
                path = path[0:path.rfind("/")]

            # Change the path
            else:
                dir_name = command[5:]              # Get name of directory
                path = path + "/" + dir_name        # Add to the path
                dirs.update({path:0})               # Update our dictionary

    
    # Do nothing when listing directories available
    elif command[0:3] == "dir":
        pass

    else:
        size = int(command[:command.find(" ")])     # Get size of file
        
        # Update size for every directory down to /home
        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]


total = 0

# space required - space unused (total space - space used)
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []

# Iterate through every path
for dir in dirs:
    
    # ==== PART 1 ====
    if dirs[dir] < 100000:
        total += dirs[dir]
    
    # ==== PART 2 ====
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])

smallest = min(valid_dirs)

print("Answer to part 1: ", total)
print("Answer to part 2: ", smallest)
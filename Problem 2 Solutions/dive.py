with open ('directions.txt') as f:
    directions_raw = f.readlines()
    directions = [direction.strip("\n") for direction in directions_raw]


# Part 1: Multiply horizontal position and vertical position after going through list of instructions
h_pos = 0
depth = 0
for direction in directions:
    vector, move = direction.split(" ")[0], int(direction.split(" ")[1])

    if vector == 'forward':
        h_pos += move
    elif vector == 'down':
        depth += move
    else:
        depth -= move

print(h_pos * depth)

# Part 2: Adds new element, "aim" which must also be calculated and changes how the other instructions interact with each other.
aim = 0
h_pos = 0
depth = 0
for direction in directions:
    vector, move = direction.split(" ")[0], int(direction.split(" ")[1])

    if vector == 'forward':
        h_pos += move
        depth += aim * move
    elif vector == 'down':
        aim += move
    else:
        aim -= move

print(h_pos * depth)
""" Solution to Day 3 of 2019 Advent of Code - https://adventofcode.com/2019/day/3 """

def wire_set_to_points(wire_set):
    ''' This function takes in a list of wires and returns a dict of points that the wire covers. '''
    return_points = {} 
    current_x = 0
    current_y = 0
    step = 0
    for coord in wire_set:
        direction = coord[0]
        distance = int(coord[1:])
        for i in range(distance):
            step += 1
            if direction == "R":
                current_x += 1
            elif direction == "L":
                current_x -= 1
            elif direction == "U":
                current_y += 1
            elif direction == "D":
                current_y -= 1
            if (current_x, current_y) not in return_points:
                return_points[(current_x, current_y)] = step
    return return_points

with open('3.txt') as f:
    lines = f.readlines()
f.close()

wire_set1 = wire_set_to_points(lines[0].split(","))
wire_set2 = wire_set_to_points(lines[1].split(","))
intersection_set = [value for value in wire_set1 if value in wire_set2]

manhattan = min(abs(x) + abs(y) for (x,y) in intersection_set)

print("3a ->", manhattan)

minsteps = min(wire_set1[point] + wire_set2[point] for point in intersection_set)

print("3b ->", minsteps)

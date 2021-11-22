""" Solution to Day 12 of 2019 Advent of Code - https://adventofcode.com/2019/day/12 """

import re
import numpy as np

def update_velocity(position, velocity):
    for counti, item in enumerate(position):
        for countc, compare in enumerate(position):
            if counti < countc:
                if item[0] > compare[0]:
                    velocity[counti][0] = velocity[counti][0] - 1
                    velocity[countc][0] = velocity[countc][0] + 1
                if item[0] < compare[0]:
                    velocity[counti][0] = velocity[counti][0] + 1
                    velocity[countc][0] = velocity[countc][0] - 1
                if item[1] > compare[1]:
                    velocity[counti][1] = velocity[counti][1] - 1
                    velocity[countc][1] = velocity[countc][1] + 1
                if item[1] < compare[1]:
                    velocity[counti][1] = velocity[counti][1] + 1
                    velocity[countc][1] = velocity[countc][1] - 1
                if item[2] > compare[2]:
                    velocity[counti][2] = velocity[counti][2] - 1
                    velocity[countc][2] = velocity[countc][2] + 1
                if item[2] < compare[2]:
                    velocity[counti][2] = velocity[counti][2] + 1
                    velocity[countc][2] = velocity[countc][2] - 1

    return velocity

def update_position(position, velocity):
    for countx, item in enumerate(position):
        for county, compare in enumerate(item):
            position[countx][county] = position[countx][county] + velocity[countx][county]
    return position

def energy_sum(position, velocity):
    total_energy = 0
    for countx, item in enumerate(position):
        total_position = 0
        total_velocity = 0
        for individual in item:
            total_position = total_position + abs(individual)
        for individual in velocity[countx]:
            total_velocity = total_velocity + abs(individual)
        total_energy = total_energy + total_velocity * total_position
    return total_energy

def main():
    position_list = []

    try:
        with open('12.txt') as f:
            lines = f.readlines()

    except IOError:
        print("Could not read file:", file1)

    for line in lines:
        line = line.strip()
        temp_values = line.split(",")
        temp_position = []
        for item in temp_values:
            item = item.strip()
            value = re.split("=|>",item)
            temp_position.append(int(value[1]))
        position_list.append(temp_position)

    velocity_list = [[0 for j in range(3)] for i in range(4)] 
    for i in range(1000):
        velocity_list = update_velocity(position_list,velocity_list)
        position_list = update_position(position_list,velocity_list)
    answer = energy_sum(velocity_list,position_list)

    print("12a -> ",answer)

    position_list = []

    try:
        with open('12.txt') as f:
            lines = f.readlines()

    except IOError:
        print("Could not read file:", file1)

    for line in lines:
        line = line.strip()
        temp_values = line.split(",")
        temp_position = []
        for item in temp_values:
            item = item.strip()
            value = re.split("=|>",item)
            temp_position.append(int(value[1]))
        position_list.append(temp_position)

    velocity_list = [[0 for j in range(3)] for i in range(4)]

    x_axis, y_axis, z_axis = set(), set(), set()
    counter = 0
    while True:
        velocity_list = update_velocity(position_list,velocity_list)
        position_list = update_position(position_list,velocity_list)        
        x_loc, y_loc, z_loc = "","","" 
        counter += 1
        for item in velocity_list:
            x_loc = x_loc + str(item[0])
            y_loc = y_loc + str(item[1])
            z_loc = z_loc + str(item[2])

        for item in position_list:
            x_loc = x_loc + str(item[0])
            y_loc = y_loc + str(item[1])
            z_loc = z_loc + str(item[2])

        if x_loc in x_axis and y_loc in y_axis and z_loc in z_axis:
            break

        x_axis.add(x_loc)
        y_axis.add(y_loc)
        z_axis.add(z_loc)

    solution = np.lcm(len(x_axis),np.lcm(len(y_axis),len(z_axis)))

    print("12b -> ",solution)

if __name__ == "__main__":
    main()

""" Solution to Day 10 of 2019 Advent of Code - https://adventofcode.com/2019/day/10 """

import math

def initializer(): # slurp in all the asteroids as (x, y) pairs
    with open('10.txt') as f:
        for y, line in enumerate(f.readlines()):
            for x, a in enumerate(line):
                if a == '#':
                    yield (x, y)

def angler(start, end):
    # this first line is a bit of a kludge, just calculating atan in radians & converting to degrees
    result = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi 
    if result < 0:
        return 360 + result
    return result

asteroids = list(initializer())

result = None
max = 0

for startpoint in asteroids:
    # another kludge, just iterating through all start points, then all end points for each start
    # goal is to get a count for all asteroids visible from that start point, and using a dict
    # ensures uniques
    cnt = len({angler(startpoint, endpoint) for endpoint in asteroids if startpoint != endpoint}) 
    if cnt > max:
        max = cnt
        result = startpoint

print("10a -> ",max)

asteroids.remove(result)

# build an array of angles and points and sort them by angle
# this lets us easily run through them and blow up asteroids!
angles = sorted(
    ((angler(result, end), end) for end in asteroids),
      key=lambda x: (x[0], abs(result[0] - x[1][0]) + abs(result[1] - x[1][1]))
)

index = 0
last = angles.pop(index)
last_angle = last[0]
count = 1

# blow up the first 199 asteroids
while count < 200 and angles:
    if index >= len(angles): # if we get all the way around and we still need to blow up more
        index = 0
        last_angle = None
    if last_angle == angles[index][0]: # if the next asteroid in the index is at the exact angle of the current one
        index += 1
        continue
    last = angles.pop(index) # pew pew
    last_angle = last[0] # pew pew pew
    count += 1

answer = last[1][0] * 100 + last[1][1]

print("10b -> ",answer)

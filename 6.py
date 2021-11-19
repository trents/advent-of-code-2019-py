""" Solution to Day 6 of 2019 Advent of Code - https://adventofcode.com/2019/day/6 """

with open('6.txt') as temp_file:
  lines = [line.rstrip('\n') for line in temp_file]

orbits = {}
orbital_seq = {}
orbits["COM"] = 0
orbital_seq["COM"] = "COM"

while len(lines) > 0:
    item = lines.pop(0)
    orbitz = item.split(")")
    if orbitz[0] not in orbits:
       lines.append(item)
    else:
       orbits[orbitz[1]] = orbits[orbitz[0]] + 1
       orbital_seq[orbitz[1]] = orbital_seq[orbitz[0]] + ")" + orbitz[1]

tree_count = 0

for value in orbits.values():
    tree_count += value

orbital_you = orbital_seq["YOU"].split(")")
orbital_san = orbital_seq["SAN"].split(")")

trunk = 0

while orbital_you[trunk] == orbital_san[trunk]:
    trunk += 1

distance = orbits["SAN"] + orbits["YOU"] - (trunk * 2)

print("6a ->",tree_count)
print("6b ->",distance)

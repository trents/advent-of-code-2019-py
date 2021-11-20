""" Solution to Day 8 of 2019 Advent of Code - https://adventofcode.com/2019/day/8 """

with open('8.txt') as temp_file:
  lines = [line.rstrip('\n') for line in temp_file]

layers = [lines[0][i:i+150] for i in range(0, len(lines[0]), 150)]

fewest_0_digits_layer = ""
min_zeros = 999999

for layer in layers:
    tempcount = layer.count('0')
    if tempcount < min_zeros:
        min_zeros = tempcount
        fewest_0_digits_layer = layer

min_layer_prod = fewest_0_digits_layer.count('1') * fewest_0_digits_layer.count('2')

print("8a -> ",min_layer_prod)

master_layer = layers[0]

for count, layer in enumerate(layers):
    for i, char in enumerate(layer):
        if master_layer[i] == "2":
            if char == "0" or char == "1":
                master_layer = master_layer[0:i] + char + master_layer[i+1:150]

master_layer = master_layer.replace("0"," ")
master_layer = master_layer.replace("1","X")

print("8b ->")
print(master_layer[0:24])
print(master_layer[25:49])
print(master_layer[50:74])
print(master_layer[75:99])
print(master_layer[100:124])
print(master_layer[125:149])

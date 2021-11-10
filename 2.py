""" Solution to Day 2 of 2019 Advent of Code - https://adventofcode.com/2019/day/2 """

with open('2.txt') as f:
    lines = f.readlines()
f.close()

program = lines[0].split(",")

for count, value in enumerate(program):
    program[count] = int(value)

current_code = 0
prog_length = len(program)
opcode = program[0]

program[1] = 12
program[2] = 2

while opcode < 99:
    value1 = program[program[current_code+1]]
    value2 = program[program[current_code+2]]
    result_place = program[current_code+3]
    if opcode == 1:
        program[result_place] = value1 + value2
    elif opcode == 2:
        program[result_place] = value1 * value2
    current_code += 4
    opcode = program[current_code]

print("2a ->",program[0])

program = lines[0].split(",")

noun = 0
verb = 0

final_output = 0

while noun < 100:
    verb = 0
    while verb < 100:
        program = lines[0].split(",")
        for count, value in enumerate(program):
            program[count] = int(value)

        current_code = 0
        prog_length = len(program)
        opcode = program[0]

        program[1] = noun
        program[2] = verb

        while opcode < 99:
            value1 = program[program[current_code+1]]
            value2 = program[program[current_code+2]]
            result_place = program[current_code+3]
            if opcode == 1:
                program[result_place] = value1 + value2
            elif opcode == 2:
                program[result_place] = value1 * value2
            current_code += 4
            opcode = program[current_code]

        if program[0] == 19690720:
            final_output = 100 * noun + verb

        verb += 1
    noun += 1

print("2b ->",final_output)

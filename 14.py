""" Solution to Day 14 of 2019 Advent of Code - https://adventofcode.com/2019/day/14 """

from collections import defaultdict

def ore_required(fuel,reactions):
    # create a dict of needed items (starting with 1 fuel) and a dict of excess items

    chemical_needs = defaultdict(int, {"FUEL": fuel})
    chemical_haves = defaultdict(int)
    ore = 0

    # keep iterating through needs until empty

    while chemical_needs:
        item = list(chemical_needs.keys())[0]

        # if we have the item we need already, use it up and restart the loop
        if chemical_needs[item] <= chemical_haves[item]:
            chemical_haves[item] -= chemical_needs[item]
            del chemical_needs[item]
            continue

        # otherwise, figure out how much more we need, then delete the wants and haves
        num_needed = chemical_needs[item] - chemical_haves[item]
        del chemical_haves[item]
        del chemical_needs[item]
        num_produced = reactions[item]["output"]

        # figure out how many reactions we need to run to produce the needed output
        if (num_needed / num_produced) == int(num_needed / num_produced):
            num_reactions = num_needed // num_produced
        else:
            num_reactions = (num_needed // num_produced) + 1
        chemical_haves[item] += (num_reactions * num_produced) - num_needed

        # if we're directly using ore, increment it; otherwise, increment the reactants
        for chemical in reactions[item]["input"]:
            if chemical == "ORE":
                ore += reactions[item]["input"][chemical] * num_reactions
            else:
                chemical_needs[chemical] += reactions[item]["input"][chemical] * num_reactions

    return ore

def main():
    try:
        with open('14.txt') as f:
            lines = list(map(str.strip, f.readlines()))

    except IOError:
        print("Could not read file:", file1)

    # create a data structure to hold all the reactions

    reactions = {}

    for reaction in lines:
        input, output = reaction.split(" => ")
        output_number, output_chemical = output.split(" ")
        inputs = {}
        for input_string in input.split(", "):
            input_number, input_chemical = input_string.split(" ")
            inputs[input_chemical] = int(input_number)
        output_number = int(output_number)
        reactions[output_chemical] = {"output": output_number, "input": inputs}

    print("14a -> ",ore_required(1,reactions))

    # iterate toward solution for 1000000000000 ore
    # start by coming up with a reasonable range of fuel produced

    low = 1000000000000 // ore_required(1,reactions)
    high = 10 * low

    # look for upper and lower bounds of fuel

    while ore_required(high,reactions) < 1000000000000:
        low = high
        high = 10 * low

    # iterate those values, honing in on maximum fuel value

    while low < (high - 1):
        mid = (low + high) // 2
        ore = ore_required(mid,reactions)
        if ore < 1000000000000:
            low = mid
        elif ore > 1000000000000:
            high = mid
        else:
            break

    print("14b -> ",int(mid)-1)

if __name__ == "__main__":
    main()

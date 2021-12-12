from numpy import amin, amax, array, absolute, where
import math
with open("code/Day_07/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

NUMBERS = [int(l) for l in lines[0].split(",")]

def part_1():
    numbers = array(NUMBERS)
    min_V = amin(numbers)
    max_v = amax(numbers)
    comsumptions = []
    positions = array(range(0,max_v+1))
    for i in range(0,max_v+1):
        moved = absolute(numbers - i)
        comsumptions.append(sum(moved))

    comsumptions = array(comsumptions)
    minimum_comsumption = comsumptions[where(comsumptions == min(comsumptions))]
    position = positions[where(comsumptions == min(comsumptions))]

    print(minimum_comsumption)
    print(position)

def part_2():
    numbers = array(NUMBERS)
    min_V = amin(numbers)
    max_v = amax(numbers)
    comsumptions = []
    positions = array(range(0,max_v+1))
    for i in range(0,max_v+1):
        moved = absolute(numbers - i)
        for j in range(moved.shape[0]):
            moved[j] = sum(range(0,moved[j]+1))
        comsumptions.append(sum(moved))

    comsumptions = array(comsumptions)
    minimum_comsumption = comsumptions[where(comsumptions == min(comsumptions))]
    position = positions[where(comsumptions == min(comsumptions))]

    print(minimum_comsumption)
    print(position)


if __name__== "__main__":
    part_1()
    part_2()
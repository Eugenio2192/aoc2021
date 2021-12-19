from numpy import array, flipud, fliplr, zeros, sum, array_split, delete
import re
with open("code/Day_13/input.txt","r", encoding="utf-8-sig") as file:
    LINES = file.readlines()

def parse(lines):
    points = [l.strip().split(",") for l in lines if re.match("[0-9]+(,[0-9]+)+", l.strip())]
    points = [(int(p[0]), int(p[1])) for p in points]
    instructions = [l.strip() for l in lines if not re.match("[0-9]+(,[0-9]+)+", l.strip())]
    instructions = [i for i in instructions if i !=""]
    instructions = [i.replace("fold along ", "").split("=") for i in instructions ]
    instructions = [(i[0], int(i[1])) for i in instructions]
    return points, instructions

def build_array(points):
    x_max = max(p[0] for p in points) +1
    y_max = max(p[1] for p in points) +1
    arr = zeros((y_max, x_max), dtype=bool)
    for p in points:
        arr[p[1], p[0]] = True
    return arr

def fold(arr, axis, coordinate):
    if axis == "y":
        flipped = arr + flipud(arr) 
        point = coordinate if (flipped.shape[0] + 1) % 2 == 0 else coordinate
        folded = flipped[:point]
    elif axis == "x":
        flipped = arr + fliplr(arr)  
        point = coordinate if (arr.shape[1] + 1) % 2 == 0 else coordinate
        folded = flipped[:, :point] 
    return folded

def part_1():
    points, instructions = parse(LINES)
    arr = build_array(points)
    folded = fold(arr, *instructions[0])
    print(arr * 1)
    print(sum(folded))
    print(folded * 1)

def part_2():
    points, instructions = parse(LINES)
    instructions.reverse()
    arr = build_array(points)
    while len(instructions) > 0:
        arr = fold(arr, *instructions.pop())
    strng = "" 
    for j in range(arr.shape[0]):
        for i in range(arr.shape[1]):
            strng +=  "#" if arr[j, i] else " "
        strng += "\n"
    print(strng)
    


if __name__ == "__main__":
    part_2()
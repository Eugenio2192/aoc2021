import re
import os
from numpy import array, zeros, ones, where, all
with open("code/Day_05/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

def parse_vectors(lines):
    pairs = [l.replace("\n", "").split(" -> ") for l in lines]
    string_elements = [[e.split(",") for e in p] for p in pairs]
    vectors = [[[int(n) for n in e] for e in p] for p in string_elements]
    return array(vectors)


def build_grid(vectors):
    numbers = [p for v in vectors for p in v]
    x_dim = max([x for x, y in numbers]) 
    y_dim = max([y for x, y in numbers]) 
    return zeros((x_dim+1, y_dim+1))

def select_straight(vectors):
    straight_vs = [v for v in vectors if any(all(v == v[0,:], axis = 0))]
    return array(straight_vs)

def part_1():
    vectors = parse_vectors(lines)
    grid = build_grid(vectors)
    straight = select_straight(vectors)
    for v in straight:
        if v[0,0] == v[1,0]:
            s = min(v[0,1],v[1,1])
            e = max(v[0,1],v[1,1])+1
            grid[v[0,0], s:e] +=1
        elif v[0,1] == v[1,1]:
            s = min(v[0,0],v[1,0])
            e = max(v[0,0],v[1,0])+1
            grid[s:e, v[0,1]] +=1
        else:
            raise ValueError("Something went wrong")
    danger_level = sum(sum((grid >= 2) * 1))
    print("The danger level is {}".format(danger_level))

def part_2():
    vectors = parse_vectors(lines)
    grid = build_grid(vectors)
    #straight = select_straight(vectors)
    for v in vectors:
        if v[0,0] == v[1,0]:
            s = min(v[0,1],v[1,1])
            e = max(v[0,1],v[1,1])+1
            grid[v[0,0], s:e] +=1
        elif v[0,1] == v[1,1]:
            s = min(v[0,0],v[1,0])
            e = max(v[0,0],v[1,0])+1
            grid[s:e, v[0,1]] +=1
        elif (v[0,1] - v[1,1]) / (v[0,0] - v[1,0]) > 0:
            s = min(v[0,0], v[1,0])
            e = max(v[0,0], v[1,0])+1 
            x0 = min(v[0,0], v[1,0])
            y0 =min(v[0,1], v[1,1])
            for i in range(0,e-x0):
                grid[x0+i, y0+i] +=1
        elif (v[0,1] - v[1,1]) / (v[0,0] - v[1,0]) < 0:
            s = min(v[0,0], v[1,0])
            e = max(v[0,0], v[1,0])+1 
            x0 = min(v[0,0], v[1,0])
            y1 =max(v[0,1], v[1,1])
            for i in range(0,e-x0):
                grid[x0+i,y1-i] +=1
        else:
            raise ValueError("Something is missing")
    danger_level = sum(sum((grid >= 2) * 1))
    print(grid.T)
    print("The danger level is {}".format(danger_level))

if __name__ == "__main__":
    part_1()
    part_2()
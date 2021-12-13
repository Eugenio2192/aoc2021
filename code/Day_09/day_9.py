from numpy import array, zeros, where
from enum import Enum
def get_input():
    with open("code/Day_09/input.txt","r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    line = lines[0].strip("\n")
    lines= [l.strip("\n") for l in lines]
    mapped = array([[int(el) for el in l] for l in lines])
    return mapped

def get_lows(data):
    low_map = zeros(data.shape)
    y_max = data.shape[0] -1 
    x_max = data.shape[1] -1
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            t = data[i, j] < data[max(0,i-1),j] if (i-1)>=0 else True
            l = data[i, j] < data[i,max(0,j-1)] if (j-1)>=0 else True
            r = data[i, j] < data[i,min(x_max,j+1)] if (j+1)<=x_max else True
            d = data[i, j] < data[min(y_max,i+1),j] if (i+1)<=y_max else True
            neighbors = [t,l,r,d]
            low_map[i,j] = all(neighbors) if all(neighbors) else False
    return low_map


class Directions(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class Robot(object):
    def __init__(self, pos_0, karte):
        self.position = pos_0
        self.direction = Directions.RIGHT
        self.karte = karte
        self.visits = zeros(karte.shape) +  11 * self.karte
        self.karte[self.position] = 1
        self.energy = 40000

    def explore(self):
        while self.energy > 0:
            self.look()
            self.go_forward()
            self.mark()
        return self.karte

    def turn_left(self):
        self.direction = Directions((self.direction.value + 1) % 4)

    def go_forward(self):
        if self.direction == Directions.RIGHT:
            self.position = (self.position[0] , self.position[1] + 1)
        elif self.direction == Directions.DOWN:
            self.position = (self.position[0] +1, self.position[1])
        elif self.direction == Directions.LEFT:
            self.position = (self.position[0], self.position[1] - 1)
        elif self.direction == Directions.UP:
            self.position = (self.position[0] - 1, self.position[1])
    
    def mark(self):
        if self.karte[self.position] == 0:
            self.karte[self.position] = 1
            self.visits[self.position] += 1
        else:
            smallest = 1000
            self.visits[self.position] += 1
            self.panic()
            self.energy -= 2**self.visits[self.position] 
    
    def look(self):
        y, x = self.position
        x_max = self.karte.shape[1]
        y_max = self.karte.shape[0] 
        condition_right = ((self.direction == Directions.RIGHT) & ((x + 1 == x_max)|(self.karte[y, min(x + 1, x_max-1)]  == 9) ))
        condition_down = ((self.direction == Directions.DOWN) & ((self.karte[min(y + 1, y_max-1) , x]  == 9)| (y + 1 == y_max)))
        condition_left =  ((self.direction == Directions.LEFT) & ((self.karte[y, x - 1]  == 9)| (x - 1 == -1)) )
        condition_up = ((self.direction == Directions.UP) & ((self.karte[y - 1 , x]  == 9)| (y - 1 == -1)))
        while  condition_right  | condition_down | condition_left | condition_up:
            self.turn_left()
            condition_right = ((self.direction == Directions.RIGHT) & ((x + 1 == x_max)|(self.karte[y, min(x + 1, x_max-1)]  == 9) ))
            condition_down = ((self.direction == Directions.DOWN) & ((self.karte[min(y + 1, y_max-1) , x]  == 9)| (y + 1 == y_max)))
            condition_left =  ((self.direction == Directions.LEFT) & ((self.karte[y, x - 1]  == 9)| (x - 1 == -1)) )
            condition_up = ((self.direction == Directions.UP) & ((self.karte[y - 1 , x]  == 9)| (y - 1 == -1))) 

    def panic(self):
        y, x = self.position
        x_max = self.karte.shape[1]
        y_max = self.karte.shape[0] 
        right_visits = self.visits[y, min(x + 1, x_max-1)] 
        up_visits = self.visits[max(y - 1, 0) , x]
        left_visits = self.visits[y, max(x - 1,0)]
        down_visits = self.visits[min(y + 1, y_max-1) , x]
        visits = [right_visits, up_visits, left_visits, down_visits]
        new_direction = visits.index(min(visits))
        self.direction = Directions(new_direction)
        


def part_1():
    data = get_input()
    low_map = get_lows(data)
    risk_levels = low_map * (data +1)
    print(risk_levels)
    print(int(risk_levels.sum()))

def part_2():
    data = get_input()
    low_map = get_lows(data)
    limits = (data == 9) * 9
    locs = where(low_map == 1)
    lower_locs = [(i,j) for i, j in zip(list(locs[0]), list(locs[1]))]
    sizes = []
    for ll in lower_locs:
        robot = Robot(ll, limits.copy())
        basin = robot.explore()
        sizes.append(sum(sum(robot.karte == 1)))
    sizes = sorted(sizes)
    print(sizes[-3:])
    print(sizes[-1] * sizes[-2] * sizes[-3])
if __name__ == "__main__":
    part_2()
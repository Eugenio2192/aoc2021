from math import copysign
from tqdm import trange
with open("code/Day_17/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

target_string = [s.split("=")[1] for s in lines[0].replace("target area: ", "").strip().split(",")]
target = [[int(n) for n in t.split("..")] for t in target_string]


def shooter(dx,dy, target,  x0=0, y0=0):
    max_height = 0
    x = x0
    y = y0
    x_range, y_range = target
    met_target = False
    for n in range(1000):
        x += dx
        y += dy
        dx += -((dx/dx) % 2 * copysign(1,dx) ) if dx != 0 else 0
        dy -=1
        max_height = max_height if y < max_height else y
        met_target = (x_range[0]<= x <= x_range[1]) & (y_range[0]<= y <=y_range[1])
        if met_target:
            return max_height, met_target

    return max_height, met_target

def grid_search():
    max_height = 0
    dx_grid = trange(20, desc="Current max: {}".format(max_height), leave=True)
    dy_grid = range(0,2000)
    dx_max = 0
    dy_max = 0
    for dx in dx_grid:
        for dy in dy_grid:
            run_max, met_target = shooter(dx, dy, target)
            if met_target:
                max_height = max_height if run_max < max_height else run_max
                dx_max = dx_max if run_max < max_height else dx
                dy_max = dy_max if run_max < max_height else dy
                dx_grid.set_description("Current max: {}".format(max_height))
    return dx_max, dy_max, max_height

def grid_search_2():
    counter = 0
    dx_grid = trange(0, 80, desc="Current count: {}| x = {} y = {}".format(counter, -200, -1000), leave=True)
    dy_grid = range(-500,500)
    
    for dx in dx_grid:
        
        for dy in dy_grid:
            dx_grid.set_description("Current count: {}| x = {} y = {}".format(counter, dx, dy))
            _ , met_target = shooter(dx, dy, target)
            if met_target:
                counter += 1
                
    return  counter


def part_1():

    dx_max, dy_max, max_height = grid_search()
    print(dx_max, dy_max, max_height )

def part_2():

    counter = grid_search_2()
    print(counter )
if __name__=="__main__":
    part_2()
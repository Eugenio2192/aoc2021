from numpy import array, where, ones, sum, ravel, all
with open("code/Day_11/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

INITAL = array([[int(octopus) for octopus in line.strip()] for line in lines])

class Octopuses(object):
    def __init__(self, grid):
        self.grid = grid.copy()
        self.counter = 0

    def step(self):
        self.grid +=1
        shinners = where(self.grid > 9)
        shine_grid = ones(self.grid.shape)
        self.shine(shinners, shine_grid)
        self.counter +=(sum(self.grid == 0))

    def shine(self, shinners, shine_grid):
        iterator  = [(i, j) for i, j in zip(shinners[0], shinners[1])]
        for i, j in iterator:
            if shine_grid[i, j] == 1:
                shine_grid[i,j] = 0
                self.collateral(i,j, shine_grid)
        shinners = where((self.grid > 9) & (shine_grid == 1)) 
        if len(shinners[0]) > 0:
            self.shine(shinners, shine_grid)
        self.grid[where(shine_grid == 0)] = 0 
    
    def collateral(self, i, j, shine_grid):
        x_max = self.grid.shape[1]
        y_max = self.grid.shape[0]
        left = (i-1) if (i-1) >= 0 else (y_max + 2)
        up = (j-1) if (j-1) >= 0 else (x_max + 2)
        for pair in [(left, up), (left,j), (left, j+1), (i, up), (i, j+1),(i+1, up), (i+1, j), (i+1,j+1)]:
            try:
                if shine_grid[pair] == 1:
                    self.grid[pair] += 1
            except IndexError:
                pass

def part_1():
    octos = Octopuses(INITAL)
    for i in range(100):
        octos.step()
    print(octos.counter)

def part_2():
    octos = Octopuses(INITAL)
    step = 0
    sync = False
    while not sync:
        
        octos.step()
        sync = all(octos.grid==0)
        step+=1
    print(step)

if __name__== "__main__":
    part_1()
    part_2()


with open("code/Day_2/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

pairs = [l.replace("\n", "").split(" ") for l in lines]
numbers = [(p[0], int(p[1])) for p in pairs]

# Part 1
def part_1():
    horizontal = sum([n[1] for n in numbers if n[0] == "forward"])
    up_down = [n for n in numbers if n[0] != "forward"]
    depth = sum([ud[1] if ud[0] == "down" else -ud[1] for ud in up_down])
    print("The horizontal position is {}, the depth is {} and its product is {}".format(horizontal,  depth, horizontal * depth))

# Part 2
class Submarine(object):
    def __init__(self):
        self.h_pos = 0
        self.v_pos = 0
        self.aim = 0

    def move(self, action, magnitude):
        if action == "forward":
            self.advance(magnitude)
        elif action == "down":
            self.turn(magnitude)
        elif action == "up":
            self.turn(-magnitude)

    def advance(self, magnitude):
        self.h_pos += magnitude
        self.v_pos += magnitude * self.aim

    def turn(self, magnitude):
        self.aim += magnitude

def loop(actions):
    submarine = Submarine()
    while len(actions) != 0:
        next = actions.pop(0)
        submarine.move(*next)
    return submarine

def part_2():
    submarine = loop(numbers)
    h_pos = submarine.h_pos
    v_pos = submarine.v_pos
    print("The horizontal position is {}, the depth is {} and its product is {}".format(h_pos, v_pos, h_pos * v_pos))

if __name__ =="__main__":
    part_2()
from numpy import array, zeros, where, equal, empty_like, arange
with open("code/Day_08/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()




def part_1():
    signals = []
    outputs = []
    for line in lines:
        s, o = [l.strip().split(" ") for l in line.split("|")]
        signals.append(s)
        outputs.append(o)
    count = 0
    for o in outputs:
        count+= sum([1 for e in o if len(e) == 3])
        count+= sum([1 for e in o if len(e) == 2])
        count+= sum([1 for e in o if len(e) == 4])
        count+= sum([1 for e in o if len(e) == 7])
    print(count)

functional_map = array(
    #    A,B,C,D,E,F,G
    [
        [1,1,1,0,1,1,1], #0
        [0,0,1,0,0,1,0], #1
        [1,0,1,1,1,0,1], #2
        [1,0,1,1,0,1,1], #3
        [0,1,1,1,0,1,0], #4
        [1,1,0,1,0,1,1], #5
        [1,1,0,1,1,1,1], #6
        [1,0,1,0,0,1,0], #7
        [1,1,1,1,1,1,1], #8
        [1,1,1,1,0,1,1], #9
    ]
)
initial_order = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
}
identifiers = dict(zip(list(initial_order.keys()), [functional_map[:,i] for i in range(functional_map.shape[1])]))

def swapper(n, i, j):
    if n == i:
        return j
    elif n == j:
        return i
    else:
        return n

class Display(object):

    def __init__(self, signals, outputs):
        self.signals  = signals
        self.outpus = outputs
        self.map = zeros((10, 7))

    def initial_assign(self):
        known = []
        for i, l in [(1,2), (7,3),(4, 4), (8, 7)]:
            code = [e for e in self.signals if len(e) == l][0]
            known.append(code)
            for letter in code:
                self.map[i, initial_order[letter.capitalize()]] = 1
        j = 0
        for rest in [e for e in self.signals if e not in known]:
            while j in [1,4,7,8]:
                j +=1
            print("adding " + rest + " to " + str(j))
            for letter in rest:
                self.map[j, initial_order[letter.capitalize()]] = 1
            j+=1


    def search_positions(self):
        # search for the two
        two_col = where(self.map.sum(0) == 9)[0][0]
        two_row = where(self.map[:, two_col]== 0)[0][0]
        permutation = [swapper(n,2,two_row) for n in range(10)]
        idx = empty_like(permutation)
        idx[permutation] = arange(len(permutation))
        self.map = self.map.T[:, idx].T
        





def part_2():
    signals = []
    outputs = []
    for line in lines:
        s, o = [l.strip().split(" ") for l in line.split("|")]
        signals.append(s)
        outputs.append(o)

    display = Display(signals[0], outputs[0])
    display.initial_assign()
    display.search_positions()
    print(display.map)

if __name__ == "__main__":
    part_2()
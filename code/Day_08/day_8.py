from numpy import array, zeros, where, equal, empty_like, arange, apply_along_axis
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

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

class Display(object):

    def __init__(self, signals, outputs):
        self.signals  = signals
        self.outpus = outputs
        self.ordered = signals.copy()
        self.map = zeros((10, 7))

    def initial_assign(self):
        j = 0
        for rest in [e for e in self.signals]:
            # while j in [1,4,7,8]:
            #     j +=1
            #print("adding " + rest + " to " + str(j))
            for letter in rest:
                self.map[j, initial_order[letter.capitalize()]] = 1
            j+=1

        for i, l in [(1,2), (7,3),(4, 4), (8, 7)]:
            code = [e for e in self.ordered if len(e) == l][0]
            position_known =  self.ordered.index(code)
            self.reorder(position_known, i)
            # self.ordered = swapPositions(self.ordered, position_known, i)
            # permutation = [swapper(n,i,position_known) for n in range(10)]
            # idx = empty_like(permutation)
            # idx[permutation] = arange(len(permutation))
            # self.map = self.map.T[:, idx].T

    def reorder(self, i, j):
        permutation = [swapper(n,i,j) for n in range(10)]
        idx = empty_like(permutation)
        idx[permutation] = arange(len(permutation))
        self.map = self.map.T[:, idx].T
        self.ordered = swapPositions(self.ordered, i, j)

        

    def search_positions(self):
        # search for the two
        two_col = where(self.map.sum(0) == 9)[0][0]
        two_row = where(self.map[:, two_col]== 0)[0][0]
        self.reorder(2, two_row)
        # search for the six
        six_col = where((self.map.sum(0) == 8) & (self.map[1] == 1))[0][0]
        six_row = where((self.map[:, six_col]== 0) & (self.map.sum(1) == 6))[0][0]
        self.reorder(6, six_row)
        # search the nine 
        #nine_col = where((self.map.sum(0) == 8) & (self.map[1] == 0))[0][0]
        four_indexes = where (self.map[4] == 0)[0]
        nine_row = where(apply_along_axis(any, 1, self.map[:,four_indexes] == 0)& (self.map.sum(1) == 6))[0][0]
        self.reorder(9, nine_row)
        pass
        # search zero
        zero_row = [e for e in where((self.map.sum(1) == 6))[0] if e not in [6,9]][0]
        self.reorder(0, zero_row)
        # search three
        one_indexes = where (self.map[1] == 1)[0]
        three_row = where(apply_along_axis(all, 1, self.map[:,one_indexes] == 1)& (self.map.sum(1) == 5))[0][0]
        self.reorder(3, three_row)

    def decode(self, letters):
        code = [c for c in self.ordered if (len(c) == len(letters) and all([(l in letters) for l in c]))][0]
        return self.ordered.index(code)

    def get_output(self):
        out= ""
        for el in self.outpus:
            out += "{}".format(self.decode(el))
        return out
    





def part_2():
    signals = []
    outputs = []
    for line in lines:
        s, o = [l.strip().split(" ") for l in line.split("|")]
        signals.append(s)
        outputs.append(o)
    displays = [Display(s, o) for s, o in zip(signals,outputs)]
    values = []
    for d in displays:
        d.initial_assign()
        d.search_positions()
        values.append(int(d.get_output()))

    print(sum(values))
if __name__ == "__main__":
    part_2()
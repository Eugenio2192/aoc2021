from itertools import combinations
with open("code/Day_14/input.txt","r", encoding="utf-8-sig") as file:
    LINES = file.readlines()

STATE_0 = LINES[0].strip()

PAIRS = [l.strip().split(" -> ") for l in LINES[2:]]
CONVERTER = {p[0]: p[1] for p in PAIRS}
# [val for sublist in matrix for val in sublist]
def part_1():
    n = 40
    leters = list(CONVERTER.values())
    leter_counter = {l: 0 for l in leters}
    for element in STATE_0:
        leter_counter[element] += 1
    combs = set([c[0] +c[1] for c in list(combinations(leters, 2))])
    keys = CONVERTER.keys()
    assert len([c for c in combs if c not in keys]) == 0, "The combinations do not match"
    real_converter = {k: [k[0] + v, v + k[1]] for k, v in CONVERTER.items()}
    initial_pairs = [STATE_0[i:i+2] for i in range(len(STATE_0)-1)]
    counter = {k: 0 for k in keys}
    for iv in initial_pairs:
        counter[iv] +=1
    
    for i in range(n):
        added = {k: 0 for k in keys}
        for k in keys:
            leter_counter[CONVERTER[k]] += counter[k]
            for new in real_converter[k]:
                added[new] += counter[k]
        counter = added



    print(leter_counter)
    print(max(leter_counter.values()) - min(leter_counter.values()))
 


if __name__ == "__main__":
    part_1()
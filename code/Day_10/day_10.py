with open("code/Day_10/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    
LINES = [l.strip() for l in lines]


MATCHER = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}

VALUES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

POINTS= {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def is_corrupted(line):
    openers = []
    for chr in line:
        if chr in MATCHER.keys():
            openers.append(chr)
        elif chr in MATCHER.values():
            correct = MATCHER[openers.pop()]
            if chr != correct:
                return chr
    return False

def complete(line):
    openers = []
    for chr in line:
        if chr in MATCHER.keys():
            openers.append(chr)
        elif chr in MATCHER.values():
            openers.pop()
    return [MATCHER[o] for o in openers]

def part_1():
    wrong_chars = []
    for l in LINES:
        character = is_corrupted(l)
        if character:
            wrong_chars.append(character)
    score = sum([VALUES[c] for c in wrong_chars])
    print(score)

def part_2():
    incomplete = []
    for l in LINES:
        character = is_corrupted(l)
        if not character:
            incomplete.append(l)
    scores = []
    for l in incomplete:
        completed = complete(l)
        score = 0
        completed.reverse()
        for e in completed:
            score *= 5
            score += POINTS[e]
        scores.append(score)

    sorted_scores = sorted(scores)
    winning = sorted_scores[len(sorted_scores) // 2]
    print("The winning score is {}".format(winning))
    
if __name__ == "__main__":
    part_2()
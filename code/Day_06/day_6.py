from numpy import array, where, ones, append, exp
with open("code/Day_06/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()


NUMBERS = [int(l) for l in lines[0].split(",")]
def part_1():
    N_DAYS = 80
    numbers = NUMBERS.copy()
    print(numbers)
    for day in range(N_DAYS):
        new = len([z for z in numbers if z == 0])
        numbers_no_z = [z for z in numbers if z != 0]
        numbers_no_z = [n - 1 for n in numbers_no_z]
        numbers = numbers_no_z + [8] * new  + [6] * new

def part_2():
    N_DAYS = 50
    numbers = array(NUMBERS)
    counter = dict(zip(list(range(9)), [0] * 9))
    for n in numbers:
        counter[n] += 1
    for day in range(N_DAYS):
        zeros = counter[0]
        for i in range(1,9):
            counter[i-1] = counter[i]
        counter[8] = zeros 
        counter[6] += zeros

    total = sum([v for k, v in counter.items()])

    print(total)
    print(counter)


if __name__ =="__main__":
    part_1()
    part_2()
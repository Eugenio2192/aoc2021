with open("code/Day_1/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

numbers = [int(l.replace("\n", "")) for l in lines]

def part_1():
    s = 0
    for i, n in enumerate(numbers):
        if i < len(numbers)-1:
            if n < numbers[i+1]:
                s += 1
    print(s)

def part_2():
    s = 0
    for i in range(len(numbers)):
        if len(numbers)-i> 2:
            if (sum(numbers[i:i+3])) < (sum(numbers[i+1:i+4])):
                s+=1
    print(s)
        

if __name__ =="__main__":
    part_2()
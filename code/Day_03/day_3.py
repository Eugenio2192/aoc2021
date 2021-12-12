with open("code/Day_3/input.txt","r", encoding="utf-8-sig") as file:
    lines = file.readlines()

numbers = [l.replace("\n", "") for l in lines]

def part_1():
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(numbers[0])):
        sum_0 = sum([1 for n in numbers if int(n[i]) == 0])
        sum_1 = sum([1 for n in numbers if int(n[i]) == 1])
        gamma_rate += "{}".format(0 if sum_0 > sum_1 else 1)
        epsilon_rate +=  "{}".format(1 if sum_0 > sum_1 else 0)
    print("The Gamma rate is {}\nThe epsilon rate is {}".format(int(gamma_rate, 2), int(epsilon_rate, 2)))
    print("The fuel consumption is {}".format(int(gamma_rate, 2) * int(epsilon_rate, 2)))

def find_rating(numbers, rating, position=0):
    if rating =="O2":
        digit = 1
    elif rating == "CO2":
        digit = 0
    if len(numbers) == 1:
        return int(numbers[0],2)
    else:
        sum_0 = sum([1 for n in numbers if int(n[position]) == 0])
        sum_1 = sum([1 for n in numbers if int(n[position]) == 1])
        if sum_0 > sum_1:
            return find_rating([n for n in numbers if n[position] == "{}".format(abs(digit-1))], rating, position+1)
        elif sum_0 <= sum_1:
            return find_rating([n for n in numbers if n[position] == "{}".format(digit)], rating, position+1)

def part_2():
    o2_rating = find_rating(numbers, "O2")
    co2_rating = find_rating(numbers, "CO2")
    print("The O2 rating is {}\nThe CO2 rating is {}".format(o2_rating, co2_rating))
    print("The life support rating is {}".format(o2_rating * co2_rating))

if __name__ =="__main__":
    part_1()
    part_2()
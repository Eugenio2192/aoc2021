def hex_to_bin(hex):
    SCALE = 16
    #binary = bin(int(hex, SCALE))[2:].zfill(4)
    binary = bin(int('1'+hex,SCALE))[3:]
    return binary

with open("code/Day_16/input.txt","r", encoding="utf-8-sig") as file:
    BITS = hex_to_bin(file.read())

def count_versions(initial=0):
    i = initial
    version_count = int(BITS[i:i+3],2)
    id = int(BITS[i+3:i+6],2) 
    i += 6
    if id == 4:
        not_last = True
        while not_last:
            i += 5
            not_last = BITS[i-5] != "0"
    else:
        if BITS[i] == '0':
            last_point =  i + 16 + int(BITS[i+1:i+16],2)
            i += 16
            while i < last_point:
                i ,this_version = count_versions(i)
                version_count += this_version
        else:
            number = int(BITS[i+1:i+12],2)
            i += 12
            for j in range(number):
                i ,this_version = count_versions(i)
                version_count += this_version
    return i, version_count

def multiply(values):
    out = 1
    for v in values:
        out = out * v
    return out

OP_DICT = {
    0 : sum,
    1: multiply,
    2: min,
    3: max,
    5: lambda values: 1 if values[0] > values[1] else 0,
    6: lambda values: 1 if values[0] < values[1] else 0,
    7: lambda values: 1 if values[0] == values[1] else 0,
}
def perform_operations(initial=0):
    i = initial
    id = int(BITS[i+3:i+6],2) 
    i += 6
    if id == 4: #literal value
        not_last = True
        value = ""
        while not_last:
            value += BITS[i+1:i+5] 
            i += 5
            not_last = BITS[i-5] != "0"
        values= int(value,2)
        return i, values 

    else:
        values = []
        if BITS[i] == '0':
            last_point =  i + 16 + int(BITS[i+1:i+16],2)
            i += 16
            while i < last_point:
                i, this_values = perform_operations(i)
                values.append(this_values)
        else:
            number = int(BITS[i+1:i+12],2)
            i += 12
            for j in range(number):
                i ,this_values = perform_operations(i)
                values.append(this_values)
    return i, OP_DICT[id](values)

def part_1():
    i, version_count = count_versions()
    print(version_count)

def part_2():
    i, values = perform_operations()
    print(values)

if __name__ == "__main__":
    part_2()
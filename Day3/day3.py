from string import ascii_letters

with open('Day3/input.txt') as f:
    data = f.read().splitlines()
    sum = 0
    for line in data:
        pack1, pack2 = line[:len(line)//2], line[len(line)//2:]
        commonality = (set(pack1) & set(pack2)).pop()
        sum += ascii_letters.index(commonality) + 1
    print(sum)
    sum = 0
    for i in range(0,len(data)-2,3):
        commonality = (set(data[i]) & set(data[i+1]) & set(data[i+2])).pop()
        sum += ascii_letters.index(commonality) + 1
    print(sum)
with open('Day4/input.txt') as f:
    data = f.read().splitlines()
    data = [[[int(i) for i in pair.split('-')] for pair in line.split(',')] for line in data]
    print(sum((a <= x <= y <= b) or (x <= a <= b <= y) for (a,b), (x,y) in data))
    print(sum([max(a, x) <= min(b, y) for (a,b), (x,y) in data]))
    
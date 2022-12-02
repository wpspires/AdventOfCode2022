with open('Day1/input.txt') as f:
    data = f.read().split('\n\n')
    result = [sum([int(x) for x in y.splitlines()]) for y in data]
    result.sort(reverse=True)
    print(result[0])
    print(sum(result[:3]))
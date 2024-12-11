import sys
from rich import print as rprint
from collections import Counter, defaultdict


def f(stone):
    str_s = str(stone)
    if stone == 0:
        return [1]
    elif len(str_s) % 2 == 0:
        return [int(str_s[:len(str_s) // 2]), int(str_s[len(str_s) // 2:])]
    else:
        return [stone * 2024]

def blink(stones):
    new_stones = defaultdict(int)
    for s, count in stones.items():
        str_s = str(s)
        if s == 0:
            new_stones[1] += count
        elif len(str_s) % 2 == 0:
            new_stones[int(str_s[:len(str_s) // 2])] += count
            new_stones[int(str_s[len(str_s) // 2:])] += count
        else:
            new_stones[s * 2024] += count
    return new_stones
 
def p1(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    stones = [int(x) for x in lines[0].split(' ')]
    stones = Counter(stones)
    for _ in range(25):
        stones = blink(stones)
    print(sum(stones.values()))

def p2(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    stones = [int(x) for x in lines[0].split(' ')]
    stones = Counter(stones)
    for _ in range(75):
        stones = blink(stones)
    print(sum(stones.values()))
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
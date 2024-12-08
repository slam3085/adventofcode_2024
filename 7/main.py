import sys
from rich import print as rprint
from tqdm import tqdm

def check(res, numbers, ops):
    t = numbers[0]
    for i in range(1, len(numbers)):
        if ops[i - 1] == '+':
            t += numbers[i]
        elif ops[i - 1] == '*':
            t *= numbers[i]
        elif ops[i - 1] == '|':
            t = int(str(t) + str(numbers[i]))
    return res == t

def generate_all_variants(numbers, possible_ops):
    ops_variants = [[]]
    for _ in range(len(numbers) - 1):
        new_ops_variants = []
        for ops in ops_variants:
            for op in possible_ops:
                new_ops_variants.append([op for op in ops] + [op])
        ops_variants = new_ops_variants
    return ops_variants
 
def p1(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            res, numbers = line.split(': ')
            res = int(res)
            numbers = [int(x) for x in numbers.split(' ')]
            lines.append((res, numbers))
    ans = 0
    for res, numbers in tqdm(lines):
        for ops in generate_all_variants(numbers, ['+', '*']):
            if check(res, numbers, ops):
                ans += res
                break
    print(ans)

def p2(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            res, numbers = line.split(': ')
            res = int(res)
            numbers = [int(x) for x in numbers.split(' ')]
            lines.append((res, numbers))
    ans = 0
    for res, numbers in tqdm(lines):
        for ops in generate_all_variants(numbers, ['+', '*', '|']):
            if check(res, numbers, ops):
                ans += res
                break
    print(ans)
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
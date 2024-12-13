import sys
from rich import print as rprint

def check(a, b, prize):
    optimal_coins = 100500
    for i in range(0, 101):
        for j in range(101):
            res = (a[0] * i + b[0] * j, a[1] * i + b[1] * j)
            coins = 3 * i + j
            if res == prize and coins < optimal_coins:
                optimal_coins = coins
    if optimal_coins == 100500:
        return 0
    else:
        return optimal_coins

def p12(filename):
    inputs = []
    with open(filename) as f:
        for item in f.read().split('\n\n'):
            a, b, prize = item.split('\n')
            a = a.replace('Button A: ', '')
            b = b.replace('Button B: ', '')
            prize = prize.replace('Prize: ', '')
            inputs.append({
                'a': (int(a.split(', ')[0].replace('X+', '')), int(a.split(', ')[1].replace('Y+', ''))),
                'b': (int(b.split(', ')[0].replace('X+', '')), int(b.split(', ')[1].replace('Y+', ''))),
                'prize': (int(prize.split(', ')[0].replace('X=', '')), int(prize.split(', ')[1].replace('Y=', ''))),
            })
    # part 1
    ans1 = 0
    for item in inputs:
        ans1 += check(**item)
    print(ans1)
    # part 2
    ans2 = 0
    c = 10000000000000
    for item in inputs:
        a, b, prize = item['a'], item['b'], (item['prize'][0] + c, item['prize'][1] + c)
        j = int(round((prize[0] / a[0] - prize[1] / a[1]) / (b[0] / a[0] - b[1] / a[1])))
        i = int(round(prize[0] / a[0] - j * b[0] / a[0]))
        if (a[0] * i + b[0] * j, a[1] * i + b[1] * j) == prize:
            ans2  += 3 * i + j
    print(ans2)
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p12(filename)
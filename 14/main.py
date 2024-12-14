import sys
from rich import print as rprint
from collections import defaultdict

width, height = 101, 103

def blink(robots):
    for robot_pos, robot_speed in robots:
        robot_pos[0] += robot_speed[0]
        robot_pos[1] += robot_speed[1]
        if robot_pos[0] < 0:
            robot_pos[0] += width
        elif robot_pos[0] >= width:
            robot_pos[0] -= width
        if robot_pos[1] < 0:
            robot_pos[1] += height
        elif robot_pos[1] >= height:
            robot_pos[1] -= height

def show(robots):
    grid = []
    for _ in range(height):
        grid.append([0] * width)
    for robot_pos, _ in robots:
        grid[robot_pos[1]][robot_pos[0]] += 1
    for i, line in enumerate(grid):
        grid[i] = ''.join([str(x) if x > 0 else '.' for x in line])
    for line in grid:
        rprint(line)

def p1(filename):
    robots = []
    with open(filename) as f:
        for line in f:
            robot = line.strip().split(' ')
            robot_pos = [int(x) for x in robot[0].replace('p=', '').split(',')]
            robot_speed = [int(x) for x in robot[1].replace('v=', '').split(',')]
            robots.append([robot_pos, robot_speed])
    for _ in range(100):
        blink(robots)
    a, b, c, d = 0, 0, 0, 0
    for robot_pos, _ in robots:
        if (robot_pos[0] == (width - 1) // 2) or (robot_pos[1] == (height - 1) // 2):
            continue
        if 0 <= robot_pos[0] < (width - 1) // 2:
            if 0 <= robot_pos[1] < (height - 1) // 2:
                a += 1
            else:
                b += 1
        else:
            if 0 <= robot_pos[1] < (height - 1) // 2:
                c += 1
            else:
                d += 1
    ans = a * b * c * d
    print(ans)
 
def p2(filename):
    robots = []
    with open(filename) as f:
        for line in f:
            robot = line.strip().split(' ')
            robot_pos = [int(x) for x in robot[0].replace('p=', '').split(',')]
            robot_speed = [int(x) for x in robot[1].replace('v=', '').split(',')]
            robots.append([robot_pos, robot_speed])
    for i in range(10000):
        blink(robots)
        counts = defaultdict(int)
        for robot_pos, _ in robots:
            counts[(robot_pos[0], robot_pos[1])] += 1
        overlaps = sum([v > 1 for v in counts.values()])
        if overlaps == 0:
            print(i + 1)
            show(robots)
            break
            
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
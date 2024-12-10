import sys
from rich import print as rprint

def get_neighbours(cur_i, cur_j, grid):
    candidates = [(cur_i+1, cur_j), (cur_i-1, cur_j), (cur_i, cur_j+1), (cur_i, cur_j-1)]
    candidates = [(i, j) for i, j in candidates if 0 <= i < len(grid) and 0 <= j < len(grid[0])]
    candidates = [(i, j) for i, j in candidates if grid[i][j] - grid[cur_i][cur_j] == 1]
    return candidates

def dfs(i, j, grid):
    reached = set()
    n_paths = 0
    neighbours = get_neighbours(i, j, grid)
    while neighbours:
        new_neighbours = []
        for n_i, n_j in neighbours:
            if grid[n_i][n_j] == 9:
                reached.add((n_i, n_j))
                n_paths += 1
            new_neighbours += get_neighbours(n_i, n_j, grid)
        neighbours = new_neighbours
    return reached, n_paths

def p12(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])
    start_points = []
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch == 0:
                start_points.append((i, j))
    total_scores, total_paths = 0, 0
    for s_i, s_j in start_points:
        reached, n_paths = dfs(s_i, s_j, grid)
        total_scores += len(reached)
        total_paths += n_paths
    print(total_scores)
    print(total_paths)
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p12(filename)
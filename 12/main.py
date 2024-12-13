import sys
from rich import print as rprint

def get_neighbours(cur_i, cur_j, grid, visited):
    candidates = [
        (cur_i+1, cur_j), 
        (cur_i-1, cur_j), 
        (cur_i, cur_j+1), 
        (cur_i, cur_j-1)
    ]
    candidates = [(i, j) for i, j in candidates if 0 <= i < len(grid) and 0 <= j < len(grid[0])]
    candidates = [(i, j) for (i, j) in candidates if grid[cur_i][cur_j] == grid[i][j]]
    candidates = [c for c in candidates if c not in visited]
    return set(candidates)

def dfs(i, j, grid):
    visited = set()
    visited.add((i, j))
    neighbours = get_neighbours(i, j, grid, visited)
    while neighbours:
        new_neighbours = set()
        for n_i, n_j in neighbours:
            visited.add((n_i, n_j))
            new_neighbours |= get_neighbours(n_i, n_j, grid, visited)
        neighbours = new_neighbours
    return visited

def perimeter(figure, grid):
    perimeter = 0
    for i, j in figure:
        candidates = [
            (i+1, j), 
            (i-1, j), 
            (i, j+1), 
            (i, j-1)
        ]
        for i, j in candidates:
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or (i, j) not in figure:
                perimeter += 1
    return perimeter

def calc_upper_lower_sides(figure, figure_sorted, sign):
    # find all points with edges
    has_bound = [(i, j) for i, j in figure_sorted if (i + sign, j) not in figure]
    # union points to evaluate sides correctly
    has_bound_compressed = []
    k = 0
    while k < len(has_bound):
        i, j = has_bound[k]
        has_bound_compressed.append((i, j))
        while k + 1 < len(has_bound) and has_bound[k + 1][0] == i and has_bound[k + 1][1] - j == 1:
            k += 1
            i, j = has_bound[k]
        k += 1
    return len(has_bound_compressed)

def calc_left_right_sides(figure, figure_sorted, sign):
    # find all points with edges
    has_bound = [(i, j) for i, j in figure_sorted if (i, j + sign) not in figure]
    # union points to evaluate sides correctly
    has_bound_compressed = []
    k = 0
    while k < len(has_bound):
        i, j = has_bound[k]
        has_bound_compressed.append((i, j))
        while k + 1 < len(has_bound) and has_bound[k + 1][1] == j and has_bound[k + 1][0] - i == 1:
            k += 1
            i, j = has_bound[k]
        k += 1
    return len(has_bound_compressed)

def p12(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    figures = {}
    all_cells = set()
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            all_cells.add((i, j))
    while all_cells:
        i, j = all_cells.pop()
        figures[(i, j, lines[i][j])] = dfs(i, j, lines)
        all_cells -= figures[(i, j, lines[i][j])]
    figures_sorted_i = {k: sorted(list(v), key=lambda x: x[0]*len(lines)+x[1]) for k, v in figures.items()}
    figures_sorted_j = {k: sorted(list(v), key=lambda x: x[1]*len(lines[0])+x[0]) for k, v in figures.items()}
    squares = {k: len(v) for k, v in figures.items()}
    perimeters = {k: perimeter(v, lines) for k, v in figures.items()}
    sides = {
        k: 
        calc_upper_lower_sides(v, figures_sorted_i[k], 1) +\
        calc_upper_lower_sides(v, figures_sorted_i[k], -1) +\
        calc_left_right_sides(v, figures_sorted_j[k], 1) +\
        calc_left_right_sides(v, figures_sorted_j[k], -1)
        for k, v in figures.items()
    }
    res_1 = 0
    res_2 = 0
    for k in squares:
        res_1 += squares[k] * perimeters[k]
        res_2 += squares[k] * sides[k]
    print(res_1)
    print(res_2)
 
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p12(filename)
import sys

rotate_map = {
    'u': 'r',
    'r': 'd',
    'd': 'l',
    'l': 'u'
}
really_visited = set()
grid = []

def step(grid, i, j, direction):
    new_i, new_j = i, j
    if direction == 'u':
        new_i -= 1
    elif direction == 'd':
        new_i += 1
    elif direction == 'l':
        new_j -= 1
    elif direction == 'r':
        new_j += 1
    if not (0 <= new_i < len(grid)) or not (0 <= new_j < len(grid[0])):
        return new_i, new_j, direction
    if grid[new_i][new_j] == '.' or grid[new_i][new_j] == '^':
        return new_i, new_j, direction
    elif grid[new_i][new_j] == '#':
        return i, j, rotate_map[direction]

def p1(filename):
    with open(filename) as f:
        for line in f:
            grid.append(list(line.replace('\n', '')))
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                guard_i, guard_j = i, j
                direction = 'u'
    visited = set()
    visited.add((guard_i, guard_j))
    while True:
        guard_i, guard_j, direction = step(grid, guard_i, guard_j, direction)
        if not (0 <= guard_i < len(grid)) or not (0 <= guard_j < len(grid[0])):
            break
        visited.add((guard_i, guard_j))
    global really_visited
    really_visited |= visited
    print(len(visited))
 
def p2(filename):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '^':
                original_guard_i, original_guard_j = i, j
                original_direction = 'u'
    possible_positions = 0
    prev_i, prev_j = None, None
    for i, j in really_visited:
        if grid[i][j] != '^' and grid[i][j] != '#':
            if prev_i is not None:
                grid[prev_i][prev_j] = '.'
            prev_i, prev_j = i, j
            grid[i][j] = '#'
            guard_i, guard_j, direction = original_guard_i, original_guard_j, original_direction
            visited = set()
            visited.add((guard_i, guard_j, direction))
            while True:
                guard_i, guard_j, direction = step(grid, guard_i, guard_j, direction)
                if not (0 <= guard_i < len(grid)) or not (0 <= guard_j < len(grid[0])):
                    break
                if (guard_i, guard_j, direction) in visited:
                    possible_positions += 1
                    break
                visited.add((guard_i, guard_j, direction))
    print(possible_positions)
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
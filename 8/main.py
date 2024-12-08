import sys
from rich import print as rprint
from collections import defaultdict

def generate_antinodes(antennas, lines, min_k = 1, max_k = 1):
    antinodes = set()
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            diff_i, diff_j = antennas[j][0] - antennas[i][0], antennas[j][1] - antennas[i][1]
            k = min_k
            while (0 <= antennas[i][0] - k * diff_i < len(lines)) and (0 <= antennas[i][1] - k * diff_j < len(lines[0])):
                antinodes.add((antennas[i][0] - k * diff_i, antennas[i][1] - k * diff_j))
                k += 1
                if k > max_k:
                    break
            k = min_k
            while (0 <= antennas[j][0] + k * diff_i < len(lines)) and (0 <= antennas[j][1] + k * diff_j < len(lines[0])):
                antinodes.add((antennas[j][0] + k * diff_i, antennas[j][1] + k * diff_j))
                k += 1
                if k > max_k:
                    break
    return antinodes
 
def p1(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    all_antennas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch != '.':
                all_antennas[ch].append((i, j))
    all_antinodes = set()
    for ch, antennas in all_antennas.items():
        all_antinodes |= generate_antinodes(antennas, lines)
    print(len(all_antinodes))
 
def p2(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    all_antennas = defaultdict(list)
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch != '.':
                all_antennas[ch].append((i, j))
    all_antinodes = set()
    for ch, antennas in all_antennas.items():
        all_antinodes |= generate_antinodes(antennas, lines, min_k = 0, max_k = 1e9)
    print(len(all_antinodes))
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
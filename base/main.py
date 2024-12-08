import sys
from rich import print as rprint

 
def p1(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    print(1)
        
 
 
def p2(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    print(2)
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
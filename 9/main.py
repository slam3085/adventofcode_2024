import sys
from rich import print as rprint
from collections import deque

 
def p1(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    expanded = []
    for i, ch in enumerate(lines[0]):
        if i % 2 == 0:
            expanded += [int(i / 2)] * int(ch)
        else:
            expanded += [None] * int(ch)
    l, r = 0, len(expanded) - 1
    while l < r:
        if expanded[l] is not None:
            l += 1
        else:
            if expanded[r] is None:
                r -= 1
            else:
                expanded[l] = expanded[r]
                expanded[r] = None
                l += 1
                r -= 1
    checksum = 0
    for i, v in enumerate(expanded):
        if v is None:
            break
        checksum += i * v
    print(checksum)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
def p2(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    node_start = Node('start')
    current_node = node_start
    for i, ch in enumerate(lines[0]):
        if i % 2 == 0:
            node = Node({'value': int(i / 2), 'length': int(ch)})
        else:
            node = Node({'value': None, 'length': int(ch)})
        current_node.next = node
        current_node.next.prev = current_node
        current_node = current_node.next
    node_finish = current_node
    node_start = node_start.next
    node_start.prev = None

    cur = node_finish
    while cur != None:
        if cur.data['value'] is not None:
            # search for place to insert
            tmp = node_start
            while tmp != cur:
                # suitable place for insert
                if tmp.data['value'] is None and tmp.data['length'] >= cur.data['length']:
                    # save pointers to prev and next elements
                    tmp_next = tmp.next
                    tmp_prev = tmp.prev
                    # move block
                    moved = Node({'value': cur.data['value'], 'length': cur.data['length']})
                    tmp_prev.next = moved
                    moved.prev = tmp_prev
                    # don't forget about remained empty space
                    remained = Node({'value': None, 'length': tmp.data['length'] - cur.data['length']})
                    moved.next = remained
                    remained.prev = moved
                    remained.next = tmp_next
                    tmp_next.prev = remained
                    # clean up
                    cur.data['value'] = None
                    break
                else:
                    tmp = tmp.next
        cur = cur.prev
    
    expanded = []
    cur = node_start
    while cur:
        expanded += [cur.data['value']] * cur.data['length']
        cur = cur.next
    
    checksum = 0
    for i, v in enumerate(expanded):
        if v is None:
            continue
        checksum += i * v
    print(checksum)
    
 
if __name__ == '__main__':
    filename = 'input.txt'
    if '.txt' in sys.argv[-1]:
        filename = sys.argv[-1]
    p1(filename)
    p2(filename)
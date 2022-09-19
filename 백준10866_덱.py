import sys
from collections import deque

def process(cmd, deq):
    cmd_lst = cmd.split()
    length = len(deq)
    
    if cmd_lst[0]== 'push_front':
        deq.appendleft(cmd_lst[1])
    elif cmd_lst[0]== 'push_back':
        deq.append(cmd_lst[1])
    elif cmd_lst[0]== 'pop_front':
        if length :
            print(deq.popleft())
        else: 
            print(-1)
    elif cmd_lst[0]== 'pop_back':
        if length :
            print(deq.pop())
        else: 
            print(-1)
    elif cmd_lst[0]== 'size' :
        print(length)
    elif cmd_lst[0]== 'empty':
        if length :
            print(0)
        else: 
            print(1)
    elif cmd_lst[0]== 'front':
        if length :
            print(deq[0])
        else: 
            print(-1)
    elif cmd_lst[0]== 'back':
        if length :
            print(deq[-1])
        else: 
            print(-1)

deq = deque([])

N = int(sys.stdin.readline().split()[0])

for _ in range(N):
    cmd = sys.stdin.readline()
    process(cmd, deq)

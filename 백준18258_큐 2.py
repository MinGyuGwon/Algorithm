import sys
from collections import deque


def process(cmd, queue):
    cmd_lst = cmd.split()
    length = len(queue)
    if cmd_lst[0] == 'push':
        queue.append(int(cmd_lst[1]))
    elif cmd_lst[0] == 'pop':
        if length:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd_lst[0] == 'size':
        print(length)
    elif cmd_lst[0] == 'empty':
        if not length:
            print(1)
        else:
            print(0)
    elif cmd_lst[0] == 'front':
        if not length :
            print(-1)
        else:
            print(queue[0])
    elif cmd_lst[0] == 'back':
        if not length :
            print(-1)
        else:
            print(queue[-1])


a = sys.stdin.readline()
a = a.split()
N = int(a[0])

queue = deque([])

for _ in range(N):
    cmd = sys.stdin.readline()
    process(cmd, queue)

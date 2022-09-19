import sys
from collections import deque

N = int(sys.stdin.readline().split()[0])

lst = []
for i in range(1, N+1):
    lst.append(i)


lst = deque(lst)
for _ in range(N-1):
    lst.popleft()
    lst.append(lst.popleft())

print(lst[0])

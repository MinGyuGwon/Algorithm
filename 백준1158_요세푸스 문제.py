import sys

N, k = map(int,sys.stdin.readline().split())

lst = []

for i in range(1,N+1):
    lst.append(i)

iid = k-1

jst = []

for _ in range(len(lst)):
    try: 
        print("iid", iid)
        jst.append(lst.pop(iid))
        print()
        iid += (k-1)
        iid = iid % len(lst)
    except:
        print()

print('<'+ ', '.join(list(map(str, jst))) + '>')

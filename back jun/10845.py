import sys
N = int(sys.stdin.readline())
queue = []
for i in range(N):
    l= list(map(str,sys.stdin.readline().split()))
    if l[0] =="push":
        queue.append(l[1])
    elif l[0] =="pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif l[0] =="front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif l[0] =="size":
        print(len(queue))
    elif l[0] =="empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif l[0] =="back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    
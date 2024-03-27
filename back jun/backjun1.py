import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    l= list(map(str,sys.stdin.readline().split()))
    if l[0] =="push":
        stack.append(l[1])
    elif l[0] =="pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif l[0] =="top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif l[0] =="size":
        print(len(stack))
    elif l[0] =="empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
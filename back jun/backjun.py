import sys
N, M = map(int, sys.stdin.readline().split())
lst=list(map(int, sys.stdin.readline().split()))
max = 0
for i in range(0,N-2):
    for j in range(1+i,N-1):
        for k in range(1+j, N):
            tmp = lst[i]+lst[j]+lst[k]
            print(str(lst[i])+"/"+str(lst[j])+"/"+str(lst[k])+"/"+str(tmp))
            if tmp<= M and tmp>max:
                max = tmp
                
print(max)
import sys
import math

def main():
    l= list(map(str,sys.stdin.readline().split()))
    N = int(l[0])
    r = int(l[1])+1
    c = int(l[2])+1
    print(getsum(N,r,c))

def getsum(N,r,c):
    if r<3 and c<3:
        if r==1 and c ==1:
            return 0
        elif r ==1 and c ==2:
            return 1
        elif r ==2 and c==1:
            return 2
        elif r ==2 and c ==2:
            return 3
    if r > pow(2,N-1):
        if c> pow(2,N-1):
            return pow(pow(2,N-1),2)*3 + getsum(N-1,r-pow(2,N-1),c-pow(2,N-1))
        else:
            return pow(pow(2,N-1),2)*2 + getsum(N-1,r-pow(2,N-1),c)
    else:
        if c> pow(2,N-1):
            return pow(pow(2,N-1),2)*1 + getsum(N-1,r,c-pow(2,N-1))
        else:
            return getsum(N-1,r,c)
    
    
main()
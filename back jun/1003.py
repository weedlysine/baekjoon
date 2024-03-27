import sys

def main():
    N = int(sys.stdin.readline())
    for i in range(N):
        input = int(sys.stdin.readline())
        pivo(input)
    
def pivo(a):
    arr = [[0]*2]*41
    arr[0] = [1,0]
    arr[1] = [0,1]
    for i in range(2,a+1):
        arr[i] = [arr[i-1][0] + arr[i-2][0],arr[i-1][1] + arr[i-2][1]]
    print(str(arr[a][0])+ " "+ str(arr[a][1]))
    
    
    
main()
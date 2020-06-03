T = int(input())
N = []
l = {}
i=0
for var in range(T):
    k=[]
    N.append(int(input()))
    for i in range(len(N)):
        k = input().split(' ')
    k = set(k)
    i=i+1
    l.update(k)

ctr = ctr1 = 0
for var in range(T):
    for i in range(N):
        if N[i] % 2 != 0:
            print('Virat')
        else:
            print("Alastair")
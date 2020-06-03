T = int(input())


def mm(L):
    H = K = []
    for var in L:
        for i in range(L[1]):
            s = input().split(' ')
            H = s
        for i in range(L[2]):
            s = input().split(' ')
            K = s

        if N % 2 == 0:
            print("They can")

        else:
            print("They can't")
            break


for var in range(T):
    L = []
    N = input().split(' ')
    M = int(N[1])
    P = int(N[2])
    N = int(N[0])
    L.append(N)
    L.append(M)
    L.append(P)
    mm(L)
    continue

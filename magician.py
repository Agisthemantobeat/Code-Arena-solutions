
# # 0 <= index <= 2
# # 0 <= N <= 10000

T = int(input())
h = []
L = []
if 1 <= T <= 100:
    for var in range(T):
        N = input().split(' ')
        h.append(N[0])
        L.append(N[1])
    i = m = 0
    A = [0, 1, 2]
    for var in h:
        k = A.index(int(var))
        m = int(int(L[i]) % 2)
        ctr = ctr1 = k
        if 0 <= k <= 2:
            for j in range(m):
                ctr = ctr + 1
                if ctr >= 2:
                    ctr = 0
                # print(ctr)
                ctr1 = ctr1 - 1
                if ctr1 <= -2:
                    ctr1 = 0
                # print(ctr1)
            if A[ctr] < A[ctr1]:
                print(ctr)
            else:
                print(ctr1)

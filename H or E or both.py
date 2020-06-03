# logic wsa that if value of n/2 solutions would always be there for which EE could be formed as well as not
T = int(input())
H = []
ctr = 0
for var in range(T):
    N = int(input())
    H.append(N)
for var in range(len(H)):
    l = 1
    while l < N:
        if l == 1:
            ctr = ctr + 2
        elif l == 2:
            ctr = ctr + 3
        else:
            ctr = ctr + int(l / 2)
        l = l + 1
    print(ctr)

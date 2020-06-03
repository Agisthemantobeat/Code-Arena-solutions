# N = input().split(' ')
# Q = int(N[1])
# N = int(N[0])
#
#
# def computeGCD(x, y):
#     global gcd
#     if x > y:
#         small = y
#     else:
#         small = x
#     for i in range(1, small + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             gcd = i
#     return gcd
# M=[]
# if 1 <= N <= pow(10, 5):
#     A = input().split(' ')
# for var in range(Q):
#     M.append( int(input()))
#
# for var in range(Q):
#     h = []
#     for i in range(len(A)):
#         h.append(computeGCD(int(A[i]), M[var]))
#     h.sort()
#
#     print(h[len(A)-1])
N = input().split(' ')
Q = int(N[1])
N = int(N[0])


def computeGCD(x, y):
    global gcd
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd


M = []
if 1 <= N <= pow(10, 5) and 1 <= Q <= pow(10, 5):
     A = input().split(' ')
try:
    for var in range(Q):
        M.append(int(input()))
except EOFError:
    print('error')
for var in range(Q):
    h = []
    for i in range(len(A)):
        if 1 <= int(A[i]) <= pow(10, 6) and 1 <= M[var] <= pow(10, 6):
            h.append(computeGCD(int(A[i]), M[var]))
    h.sort()

    print(h[len(A) - 1])

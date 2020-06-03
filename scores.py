'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
T = int(input())
H = []
N = 0
ctr = 0
for var in range(T):
    L = []
    N = int(input())
    H.append(N)
    for i in range(N):
        L.append(input().split(' '))
    K.append(L)
for f, j in enumerate(K):
    for var, k in enumerate(j):
        ctr = ctr + int(k)

s = int(ctr / 3)
if ctr % 3 != 0:
    ctr = ctr + 1
else:
    ctr = ctr + 0
print(ctr)

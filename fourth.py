'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
# Write your code here T= int(input())
T = int(input())
ctr = 0
ctr1 = 0
while T <= 5 :
    if T>=1:
        T = T + 1
        N = int(input())
        B = input().split(' ')
        A = input().split(' ')
        A = sorted(A)
        B = sorted(B)
        for var in range(N):
            if A[var] > B[var]:
                ctr = ctr + 1
            elif  A[var] == B[var]:
                ctr=ctr+1
                ctr1=ctr1+1
            else:
                ctr1 = ctr1 + 1
            if ctr == ctr1 == N:
                 print('Tie')
            elif ctr == N:
                print('Bob')
            elif ctr1 == N:
                print('Alice')
            else:
                 continue

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
K = int(input())
if K >= 1 and K <= pow(10, 5):
    ctr = 0
    N = input().split(' ')
    h = sorted(N)

    if int(N[-1]) < int(h[-1]):
        print(int(h[-1]) + 1)
    else:
        print(int(h[-1]) + int(N[-1]+1))

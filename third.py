'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# # Write your code here
# K = int(input())
# if 1 <= K <= pow(10, 5):
#     ctr = 1
#     N = input().split(' ')
#     h = sorted(N)
#
#     if int(N[-1]) >= int(h[-1]):
#         print(int(h[-1]) + 1)
#     else:
#         print((int(h[-1]) + int(N[-1]) + ctr))
from pip._vendor.distlib.compat import raw_input

a = input()
b = list(map(lambda x: int(x), raw_input().split()))

dem = 1

b.sort()
c = b[::-1]

dem = 0
kq1 = 0
for i in c:
    kq = i + 2 + dem
    dem += 1
    if kq > kq1:
        kq1 = kq

print (kq1)
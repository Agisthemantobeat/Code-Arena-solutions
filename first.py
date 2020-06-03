'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import string

N = int(input())
L = []
if 1 <= N <= 10:
    for i in range(N):
        A = input()
        L.append(A)
    for var in L:
        if var.isalpha() and len(var) <= 100:
            alphabet = set(string.ascii_lowercase)
            print(alphabet)
            print(set(var.lower()))
            print(set(var.lower()) >= alphabet)


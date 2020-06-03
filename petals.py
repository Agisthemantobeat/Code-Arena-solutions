'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())
i = 0
p = [int(x) for x in input().split()]
p = sorted(p)
for var in range(N):
    k = sum(p)
    if k % 2 == 1:
        print(k)
        break
    elif var < N - 1:
        k = k - p[i]

        if k % 2 == 1:
            print(k)
            break
        elif i == N - 2:
            print(':(')
        else:
            continue
        i = i + 1
    else:
        print(':(')

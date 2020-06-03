# q1 is agroup of only men ,q2 is a group of only girls and q3 is mixed to find maximum number odf marriages  without
# being mutual friends
def p(q3):
    i = 0
    i = i + 1
    global ctr
    for var in range(q3):
        i = input().split(' ')
        A.append(i[1])
        L.append(i[0])
    for var in range(q1):
        if A.count(var) == 1:
            ctr = ctr + Y - 1
        elif L.count(var) > 1:
            ctr = ctr - 1
        if L.count(var) == 1:
            ctr = ctr + X - i
        elif L.count(var) > 1:
            ctr = ctr - 1


# Driver Code E
X = input().split(' ')
Y = int(X[1])
X = int(X[0])
q1 = int(input())
ctr = c = 0
A = []
L = []
for var in range(q1):
    i = input().split(' ')
    A.append(i[1])
    L.append(i[0])
    continue
q2 = int(input())
for var in range(q2):
    i = input().split(' ')
    A.append(i[1])
    L.append(i[0])
    continue
q3 = int(input())
m = p(q3)
print(m)

N = int(input())
s = input().split(' ')
o = int(input())
g = []
for var in range(o):
    g.append(input())
n = []
k = []
mul = 1
set1 = set(n)
set2 = set(k)
for i in s:
    if s.__contains__(i):
        continue
    else:
        n.append(i)
        k.append(s.count(i))
for var in g:
    if set(var).issubset(set1):
        for j in var:
            e = n.index(j)
            mul = int(k[e]) * mul
            k[e] = int(k[e]) - 1
    else:
        continue
    print(mul)

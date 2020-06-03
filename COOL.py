# For a number X, let its "Coolness" be defined as the number of "101"s occurring in its binary representation. For example, the number 21 has Coolness 2, since its binary representation is 101012, and the string "101" occurs twice in this representation.
#
# A number is defined as Very Cool if its Coolness is greater than or equal to K. Please, output the number of Very Cool integers between 1 and R.
#
# Input:
# The first line contains an integer T, the number of test cases.
# The next T lines contains two space-separated integers, R and K.
# Output:
# Output T lines, the answer for each test case.
# Constraints:
# 1<=T<=100
# 1<=R<=105
# 1<=K<=100
# SAMPLE INPUT
#
# 1
# 5 1
#
# SAMPLE OUTPUT
#
# 1


T = int(input())
H = []


def listToString(s):
    # initialize an empty string
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


# Driver code
for var in range(T):
    a = input().split(' ')
    H.append(a)
ctr = 0
for var, k in enumerate(H):

    i = 1
    while i < int(k[0]):
        K = []
        while i > 0:
            K.append(str(int(i % 2)))
            i = int(i / 2)
        m = listToString(K)
        print(K)
        i = i + 1

        if m.count('101', 0, len(m)) >= int(k[1]):
            ctr = ctr + 1
    print(ctr)
    if var == T - 1:
        break

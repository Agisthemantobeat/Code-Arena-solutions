# Roy frequently needs to use his old Nokia cell phone for texting whose keypad looks exactly as shown below.
#
# enter image description here
#
# You may be already familiar with the working of the keypad, however if you're not we shall see a few examples.
#
# To type "b", we need to press "2" twice. To type "?" we need to press "1" thrice. To type "5" we need to press "5"
# four times. To type "0" we need to press "0" twice.
#
# I hope that it's clear how the keypad is being used.
#
# Now Roy has lot of text messages and they are pretty lengthy. So he devised a mechanical-hand-robot (with only 1
# finger) which does the typing job. One drawback of this robot is its typing speed. It takes 1 second for single
# press of any button. Also it takes 1 second to move from one key to another. Initial position of the hand-robot is
# at key 1.
#
# So if its supposed to type "hack" it will take 1 second to move from key 1 to key 4 and then 2 seconds to type "h".
# Now again 1 second to move from key 4 to key 2 and then 1 second to type "a".
# Since "c" is present at the same key as "a" movement time is 0. So it simply takes 3 seconds to type "c".
# Finally it moves from key 2 to key 5 in 1 second and then 2 seconds to type "k". So in total it took 1+2+1+1+3+1+2= 11 seconds to type "hack".
#
# Input:
# First line contains T - number of test cases.
# Each of next T lines contain a string S - the message Roy needs to send.
# Each string is terminated by a newline escape sequence \n.
#
# Output:
# For each test case output the time taken by the hand-robot to type down the message.
#
# Constraints: 1 ≤ T ≤ 50 1 ≤ |S| ≤ 1000 , where |S| denotes the length of string S String is made of all the
# characters shown in the image above which are as follows: "." (period), "," (comma), "?" (question mark),
# "!" (exclamation mark), [a-z] (small case english alphabets), "_" (underscore) and [0-9] (digits)
#
# Note: We are using "_" underscore instead of " " empty space to avoid confusion
def fn(i, m):
    global ctr, j, s
    # print(ctr, j, s)
    if j == m:
        ctr = ctr + 0
        if var.index(i) != 0:
            ctr = ctr + 1 * (var.index(i) + 1)
        else:
            ctr = ctr + 1 * (var.index(i))
        if s == len(var) - 1:
            print(ctr)
    else:
        j = m
        ctr = ctr + 1
        if var.index(i) != 0:
            ctr = ctr + 1 * (var.index(i) + 1)
        else:
            ctr = ctr + 1 * (var.index(i))
        if s == len(var) - 1:
            print(ctr)
    s = s + 1


T = int(input())
H = []
i1 = ['.', ',', '?', '!', '1']
i2 = ['a', 'b', 'c', '2']
i3 = ['d', 'e', 'f', '3']
i4 = ['g', 'h', 'i', '4']
i5 = ['j', 'k', 'l', '5']
i6 = ['m', 'n', 'o', '6']
i7 = ['p', 'q', 'r', 's', '7']
i8 = ['t', 'u', 'v', '8']
i9 = ['w', 'x', 'y', 'z', '9']
i10 = ['/', 0]
for var in range(T):
    H.append(input())

for var in H:
    j = 1
    s = 0
    ctr = 0
    for i in var:
        if i in i1:
            m = 1
            fn(i, m)
        elif i in i2:
            m = 2
            fn(i, m)
        elif i in i3:
            m = 3
            fn(i, m)
        elif i in i4:
            m = 4
            fn(i, m)
        elif i in i5:
            m = 5
            fn(i, m)
        elif i in i6:
            m = 6
            fn(i, m)
        elif i in i7:
            m = 7
            fn(i, m)
        elif i in i8:
            m = 8
            fn(i, m)
        elif i in i9:
            m = 9
        elif i in i10:
            m = 0
            fn(i, m)

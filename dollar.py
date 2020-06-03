from datetime import datetime

import now

H = []
while True:

    n = int(input())
    k = n // 2
    s = n // 3
    m = n // 4
    if (s + k + m) > n:
        print(s + k + m)
    else:
        print(n)
    date = now.strftime("%H:%M:%S")
    # print(now.strftime("%H:%M:%S") - date)
  

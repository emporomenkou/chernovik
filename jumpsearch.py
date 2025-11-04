import math
a = input().split()
b = int(input())
index = -1
len = len(a)
for i in range(0, len) :
    a[i] = int(a[i])
a = sorted(a) 
jump = int(math.sqrt(len))
for i in range(0, len, jump) :
    if b < a[i] :
        for j in range(i - jump, i) :
            if a[j] == b :
                index = j
                break
    if len - i < jump : 
        for j in range(len - jump, len) :
            if a[j] == b :
                index = j
                break        
    if index > -1 :
        break
print(index)
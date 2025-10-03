import math
a = (input("Введите список целых чисел:")).split()
for i in range(0, len(a)) :
    a[i] = int(a[i])
ch = int(input())
match ch :
    case 0 :
        for i in range(0, len(a)) :
            a[i] = 0
        print(a)
    case 1 :
        for i in range(0, len(a)) :
             a[i] *= 2    
        print(a)    
    case 2 :
        for i in range(0, len(a), 2) :
            a[i] += 10
        print(a)
    case 3 :
        for i in range(0, len(a), 3) :
            if (a[i] < 0) :
                  a[i] = 0
                  continue
            a[i] = math.sqrt(a[i])
        print(a)
    case _ :
        s = sum(a)  
        print(s)

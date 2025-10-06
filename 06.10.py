import math
a = (input("Введите список целых чисел:")).split()
ch = int(input())
for i in range(0, len(a)) : 
    a[i] = int(a[i])


k = 0
countn = a.count(min(a))
countx = a.count(max(a))
minn = min(a)
maxx = max(a)


match ch :
    case 0 :
        if countn > 1 :
            print(minn, "- минимальный элемент. Кол-во минимальных элементов: ", countn)
        else :
            print (minn)
    case 1 :
        if countx > 1 :
            print(maxx, "- максимальный элемент. Кол-во минимальных элементов: ", countx)
        else :
            print (maxx)
    case 2 :
        b = [minn]
        for i in range(0, (maxx - minn - 1)) :
            b.append(b[i] + maxx)
        print (b)
    case 3 :
        b = [minn]
        for i in range(0, (maxx - minn - 1)) :
            b.append(b[i] * maxx)
        print (b)
    case _ :        
        m = sum(a) // len(a)
        if (m < 0) :
            print("Error. Factorial not defined for negative values :(")
        else :
            print(math.factorial(m))
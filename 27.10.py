import matplotlib.pyplot as plt 

x = range(0, 20)
y =  []
for i in x :
    y.append(i ** 2)

plt.plot(x, y)
plt.show()
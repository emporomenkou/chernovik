import pandas as pd
import numpy as np
import random
a2 = {}
for i in range(0, 10) :
    name = input()
    sname = input()
    pname = input()
    date = input()
    id = random.randint(1000000, 9999999) 
    a = {'name': name, 'surname': sname, 'parent name': pname, 'date of birth': date}
    a2.update({id:a})
# print(a2)
df = pd.DataFrame(a2.values(), index = a2.keys())
print(df)

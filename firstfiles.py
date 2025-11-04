import pandas as pd

f = open("text.txt", 'r', encoding = "UTF-8").read()
f.lower()
words = {}
text = f.split()

for i in text :
    if i in words :
        words[i] += 1
    else : 
        words.update({i:1})

letters = {}

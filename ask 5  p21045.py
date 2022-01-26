

s=[]
k= []
words = []
with open("two_cities_ascii.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
words=[x.lower()for x in words]
counts = Counter(words)
top10 = counts.most_common(10)
print("oi 10 pio dimofileis lekseis einai oi ekseis")
print(top10)
l=1
for i in range (len(words)):
    y  = words[i]
    if len(y)>2:
       p= y[:2]
       k.append(p)
   
    if len(y)>3:
         p=y[:3]
         s.append(p)
    
print("oi 3 prwtoi sundiasmoi duo prwtwn grammatwn einai") 
count = Counter(k)
top32 = count.most_common(3)
print(top32)
print("oi 3 prwtoi sundiasmoi triwn prwtwn grammatwn einai")
countt = Counter(s)
top33 = countt.most_common(3)
print(top33)
import time
from statistics import median

start = time.time()

L = []

L.insert(0, 1)
L.insert(1, 2)

for i in range (3, 48):
    L.insert((i-1), (L[i-2] + L[i-3])/(L[i-2] - L[i-3]))

srednia = sum(L)/len(L)

print ('srednia = ', srednia)
print ('mediana = ', median(L))

def all_unique(lst):
    return len(lst) == len(set(lst))

all_unique(L)
if all_unique(L) == True:
    print('nie ma elementow powtarzajacych sie')
else:
    L.sort()
    print('sa elementy powtarzjace sie, sa nimi: ')

print((time.time() - start))
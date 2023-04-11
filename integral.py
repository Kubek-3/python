import random
import numpy as np
import math
  
# granice calkowania
a = 0
b = 3

N = 1000

r = 3 # promien kola

# tablica wypelniona zerami dlugosci N
ar = np.zeros(N)
  
# losowe wartosci z przedzialu cakowania
for i in range (len(ar)):
    ar[i] = random.uniform(a,b)

calka = 0.0
drugacalka = 0.0

# funkcje do obliczenia warosci calki
def f(x):
    return np.sin(x)

def g(x):
    return math.sqrt(r*r - x*x)
  
# liczy i sumuje wartości roznych funkcji
for i in ar:
    calka += f(i)

for i in ar:
    drugacalka += 2*g(i)

wynik = (b-a)/float(N)*calka
drugiWynik = (b-a)/float(N)*drugacalka

print ("wartosc calki z sin(x) = {}.".format(wynik))
print ("wartosc calki z kola o promieniu 3 = {}.".format(drugiWynik))
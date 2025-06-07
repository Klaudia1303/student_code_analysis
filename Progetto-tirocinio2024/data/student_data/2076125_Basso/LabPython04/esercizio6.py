
from math import *

a=int(input("Inserire intero:\t"))
b=int(input("Inserire intero:\t"))
n=0
s=0


while n < abs(b):
    s=s+a
    n= n+1



if  b<0:
        s=-s

print(s)

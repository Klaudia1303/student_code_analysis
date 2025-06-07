fattoriale=1
n=int(input('inserire un numero maggiore o uguale a 0: '))
x=1
if n>=0:
      while 0<x<=n:
            fattoriale=fattoriale*x
            x=x+1
print(fattoriale)

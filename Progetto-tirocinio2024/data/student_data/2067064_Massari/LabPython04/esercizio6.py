n=int(input('inserire un intero: '))
s=int(input('inserire un intero: '))
y=1
t=n
v=s

if n==0 or s==0:
      print(0)
if n<0 and s>0:
      while y!=s:
            n+=t
            y+=1
      print('il risultato è: ',n)
if s<0 and n>0:
      while y!=n:
            s+=v
            y+=1
      print('il risultato è: ',s)
if n>0 and s>0:
      while y!=s:
            n+=t
            y+=1
      print('il risultato è: ',n)
if n<0 and s<0:
      n=-n
      s=-s
      t=-t
      v=-v
      while y!=s:
            n+=t
            y+=1
      print('il risultato è: ',n)
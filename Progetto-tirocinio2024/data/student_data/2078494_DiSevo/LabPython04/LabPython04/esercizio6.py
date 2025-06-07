x = int(input('Inserisci il primo fattore: '))
y = int(input('Inserire il secondo fattore: '))
k = 0
i = 0
if y < 0:
     while i > y:
          k -= x
          i -= 1
else:
     while i < y:
          k += x
          i += 1
print(k)

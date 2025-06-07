a = int(input("Inserire primo fattore: "))
b = int(input("Inserire secondo fattore: "))
s = 0
i = 0
if b < 0:
     while i > b:
          s -= a
          i -= 1
else:
     while i < b:
          s += a
          i += 1
print(s)

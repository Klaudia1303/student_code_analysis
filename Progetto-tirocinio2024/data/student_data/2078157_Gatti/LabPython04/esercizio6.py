n = int(input('inserisci un intero: '))
s = int(input('inserisci un intero: '))
z = 0
i = 0
if s > 0:
    while i < s:
        z = z + n 
        i += 1
if s < 0:
    while i > s:
        z = z - n
        i -= 1
print(z)

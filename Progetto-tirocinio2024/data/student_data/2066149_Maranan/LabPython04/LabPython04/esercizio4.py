i = 0
j = 0
while i < 1:
    s = int(input('Inserisci un intero (0 per terminare): '))
    if s%3==0:
        j = j + s
    if s == 0:
        i = 1
print (j)

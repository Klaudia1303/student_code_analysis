s = input('inserisci una stringa: ')
distanza_massima= 0

for i in s:
    if s.count(i) >= 2:
         distanza = s.rfind(i) - s.find(i)
        if distanza  >= distanza_massima:
            distanza_massima = distanza

print(distanza_massima)


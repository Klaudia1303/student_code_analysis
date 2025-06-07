s1 = input("Inserisci stringa --> ")
s2 = input("Inserisci stringa --> ")
massimo=""
appoggio=""
for i in range(len(s1)):
    for j in range(1,len(s1)+1):
        if s1[i:j] in s2:
            appoggio=s1[i:j]
        if len(appoggio)>len(massimo):
            massimo=appoggio
print(massimo)

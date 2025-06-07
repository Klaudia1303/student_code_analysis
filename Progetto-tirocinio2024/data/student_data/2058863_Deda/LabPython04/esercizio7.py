i=0
ripetizione=0
s=str(input('Inserisci stringa '))
while i<len(s):
    x=s[i:i+1]
    occorrenza=s.count(x)
    if occorrenza>ripetizione:
        ripetizione=occorrenza
        y=x
    elif occorrenza==ripetizione:
        y=x
    i+=1
print(y)

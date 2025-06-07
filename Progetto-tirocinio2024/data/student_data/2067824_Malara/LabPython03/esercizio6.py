s=input('inserire stringa di almeno un carattere ')
i=0
while not(i==len(s)) and ord(s[i])<100:
    i+=1
if i==len(s):
    print('stringa consumata e carattere non trovato')
else:
    print('il primo carattere Unicode > di 100 è',s[i])

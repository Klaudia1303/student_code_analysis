s=str(input())
i=0
while i<=len(s) and ord(s[i])>100:
    print(s[i])
    i=i+1
 #caso in cui i>len s o s>100
if i>len(s):
    print('stringa consumata e carattere nn trovato')
else:
    print("il primo carattere Unicode maggiore di 100 è:",s[i])

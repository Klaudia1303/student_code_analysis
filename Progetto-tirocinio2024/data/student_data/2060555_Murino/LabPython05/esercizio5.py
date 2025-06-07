s=input('inserisci una stringa contente più di due caratteri: ')
n=int(input('inserisci un intero positivo: '))
finito=True
i=0
while(i+n)<len(s):
    if s[i]==s[i+1] and finito:
        print(True)
        finito=False
    i+=1
if finito==True:
    print(False)

s= input('inserisci una stringa contenente piu di 2 caratteri: ')
n= int(input('inerisci un intero positivo: '))
finito= True
i=0
while (i+n)<len(s):
    if s[i]==s[i+n] and finito:
        print(True)
        finito=False
    i+=1
if finito ==True:
    print(False)
    

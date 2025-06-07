s=input("scrivi una stringa contenente almeno 2 caratteri: ")
n=int(input("scrivi un numero intero positivo: "))

i=0
while len(s)<2 or n<1:
    print("stringa o numero inserita/o non corrisponde alla richiesta\nInserisci di nuovo la stringa e il numero: ")
    s=input("stringa: ")
    n=int(input("numero intero positivo: "))

F=False
while i<(len(s)-n) and not F:
    if s[i]==s[i+n]:
        F=True
    i+=1
print(F)

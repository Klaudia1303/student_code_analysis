s=input("Inserisci una stringa : ")
n=int(input("Inserisci un numero intero positivo : "))
i=0
while i<len(s):
    if i+n >= len(s):
        print(False)
        break

    if s[i]==s[i+n]:
        print(True)
        break

    i+=1
    
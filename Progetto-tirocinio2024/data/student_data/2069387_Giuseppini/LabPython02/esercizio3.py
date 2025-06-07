#Scrivere un programma che prenda in ingresso un intero (a) e una stringa (s) e stampa la stringa solo se a è
#dispari

a=int(input("scrivi un intero: "))
s=input("scriv una stringa: ")
if a%2==1:
    print(s)
else:
    print('il numero è pari')

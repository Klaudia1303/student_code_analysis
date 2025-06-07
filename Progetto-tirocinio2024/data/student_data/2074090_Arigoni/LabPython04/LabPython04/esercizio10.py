a=str(input("Inserisci una stringa: "))
b=str(input("Inserisci una stringa: "))

i=True
while i:
    precedente=a
    a=str(input("Inserisci una stringa: "))
    if len(precedente)+len(b)==len(a):
        print(precedente,b,a)
        i=False

n=str(input('inserisci una stringa: '))
l=int(len(n)-1)
while not n.islower()or not n.isalpha():
    p=n[0]+n[l]
    print(p)
    n=str(input('inserisci una stringa: '))
    l=int(len(n)-1)
p=n[0]+n[l]
print(p)

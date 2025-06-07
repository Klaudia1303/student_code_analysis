c=input("Inserisci un carattere: ")
s=input("Inserisci una stringa: ")

a=0
while a<2:
    i=0
    while i<len(s):
        if s[i]==c:
            a+=1;
        i+=1
    if a>=2:
        print(s, a)
    else:
        a=0
    

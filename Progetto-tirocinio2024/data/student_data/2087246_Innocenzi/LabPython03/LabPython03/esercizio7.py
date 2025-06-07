c=input("Inserisci carattere: ")
s=input("Inserisci stringa: ")

while(s.count(c) <= 2):
    s = input("Inserisci stringa: ")
    if(s.count(c) > 2):
        print(s.count(c))
        break




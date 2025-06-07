stop=False
c=input('Inserisci carattere: ')

while not stop:
    s=input('Inserisci una stringa: ')
    counter=s.count(c)
    if counter>2:
        stop=True
print(counter)

Sprecedente=input('inserisci una stringa: ')
Sattuale=input('inserisci una stringa: ')
while Sprecedente[-1]!=Sattuale[0]:
    Sprecedente=Sattuale
    Sattuale=input('inserisci una stringa: ')
print('le ultime due stringe sono state: ', Sprecedente, Sattuale)
    

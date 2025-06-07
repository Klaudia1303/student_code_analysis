s=input('inserisci una stringa: ')
i=0
conto=0
massimo=0
ripetizioni=0
while i<len(s):
    carattere=s[i]
    ripetizioni=s.count(carattere)
    if ripetizioni>=conto:
        conto=ripetizioni
        massimo=carattere
    i=i+1
if ripetizioni==1:
    print('i caratteri sono tutti diversi')
else:
    print('il carattere ripetuto più volte è: ', massimo)


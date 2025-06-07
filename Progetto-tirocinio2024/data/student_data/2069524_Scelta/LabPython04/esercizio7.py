s=input('Inserisci una stringa: ')
i=0
n=0
while i<len(s):
    conta=s.count(s[i])
    if conta>=n:
        n=conta
        carattere=s[i]
    i+=1
print(carattere)

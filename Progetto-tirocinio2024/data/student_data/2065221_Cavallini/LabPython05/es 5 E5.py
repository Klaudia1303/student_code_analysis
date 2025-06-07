s = input('inserisci una stringa: ')
n = int(input('inserisci un numero: '))
k = False
for i in range(len(s)):
    for j in range(1,len(s)):
        if s[i]==s[j] and j-i==n:
            k=True
print(k)

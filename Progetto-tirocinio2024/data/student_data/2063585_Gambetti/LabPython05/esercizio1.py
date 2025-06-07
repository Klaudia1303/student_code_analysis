s=input('inserisci una stringa: ')
n=input('inserisci una stringa: ')
j=0
if len(s)==len(n):
    for i in range(len(s)):
        print(s[i]+n[j],end='')
        j+=1

s=str(input('inserire stringa: '))
n=int(input('inserire numero: '))
nuova_stringa=''
for i in range(len(s)):
    nuova_stringa+= s[i]*n
print(nuova_stringa)

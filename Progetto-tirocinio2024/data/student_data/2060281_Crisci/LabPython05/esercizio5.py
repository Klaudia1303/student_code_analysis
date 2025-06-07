s=str(input("Inserire una stringa di almeno due caratteri: "))
n=int(input("Inserire un intero positivo: "))
compare=False
for i in range(len(s)):
    if(i+n<len(s) and s[i]==s[i+n]):
        compare=True
print(compare)

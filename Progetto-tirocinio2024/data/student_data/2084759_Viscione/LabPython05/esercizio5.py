s=input("immetti una stringa di almeno due caratteri: ")
n=int(input("immetti un intero positivo: "))
uguali=False
for i in range(0,len(s)-n):
    if s[i]==s[i+n]:
        uguali=True
print(uguali)

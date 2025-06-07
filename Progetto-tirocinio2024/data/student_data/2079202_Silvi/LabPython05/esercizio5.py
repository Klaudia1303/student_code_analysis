import sys
s=input("inserire una stringa di almeno 2 caratteri: ")
n=int(input("inserire un numero intero positivo: "))
for i in range(0, len(s)-n):
    if s[i]==s[i+n]:
        print(True)
        sys.exit(0)
print(False)

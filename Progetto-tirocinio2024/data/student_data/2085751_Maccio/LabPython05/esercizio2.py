n=int(input("Inserire un numero intero:  "))
s=input("Inserire una stringa:  ")
for i in range(len(s)):
    print(s[i]*n, end="")

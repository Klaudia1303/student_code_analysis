s = input("Inserire una stringa (almeno 2 caratteri): ")
n = int(input("Inserire un numero intero: "))
c = False
for i in range(len(s)):
    for j in range(1,len(s)):
        if s[i]==s[j] and j-i == n:
            c = True
print(c)

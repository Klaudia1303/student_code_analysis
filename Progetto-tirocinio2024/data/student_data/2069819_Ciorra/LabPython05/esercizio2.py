s = input("Inserire una stringa; ")
n = int(input("Inserire un numero intero: "))
s3 = ''
for i in range(len(s)):
    s3 += s[i]*n
print(s3)

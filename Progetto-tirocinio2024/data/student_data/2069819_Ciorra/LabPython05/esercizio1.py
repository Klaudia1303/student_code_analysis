s1 = input("Inserire prima stringa): ")
s2 = input("Inserire seconda stringa (uguale lunghezza ad s1): ")
s3=''
for i in range (len(s1)):
    s3 += s1[i] + s2[i]
print(s3)

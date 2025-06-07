s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")
s3 = ''
for i in range(len(s1)):
    if s1[i] not in s2:
       s3 += s1[i]
print(s3)

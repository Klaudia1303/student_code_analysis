s1 = input("Inserire una stringa: ")
s2 = input("Inserire una stringa: ")
s3 = ''
for i in range(len(s1)):
    s3 = s3 + (s1[i] + s2[i])
print(s3)


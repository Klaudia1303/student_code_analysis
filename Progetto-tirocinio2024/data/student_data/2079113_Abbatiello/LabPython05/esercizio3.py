s1 = input('insersci stringa :')
s2 = input('inserisci stringa :')
i = 0
s3 =''
for i in range(len(s1)):
    if s1[i] not in s2:
        s3 = s3 + s1[i]
print(s3)

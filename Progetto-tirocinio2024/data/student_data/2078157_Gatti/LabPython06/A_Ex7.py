s1 = input('inserisci una stringa: ')
s2 = input('inserisci una stringa: ')
s3 = ''
for i in s1:
    for j in s2:
        massimo = 1
        if i == j:
            s3 += i
        else:
            continue
print(s3)

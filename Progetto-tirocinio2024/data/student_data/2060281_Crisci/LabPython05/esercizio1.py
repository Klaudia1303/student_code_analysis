s1=str(input("Inserire una stringa: "))
s2=str(input("Inserire un'altra stringa con gli stessi caratteri: "))
s3=''
for i in range(len(s1)):
    s3=s3+s1[i]+s2[i]
print(s3)

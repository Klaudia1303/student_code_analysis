s1=input('Inserire stringa: ')
s2=input('Inserire stringa: ')
n=int(input('Inserire intero: '))
s3=''
for i in s1:
    for j in s2:
      if i in s2 and (abs(s1.find(i) - s2.find(i))<=n):
          s3+=i
          break
print(s3)

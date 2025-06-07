print('Inserire due stringhe non vuote :')
s1 = input(' - prima stringa: ')
s2 = input(' - seconda stringa: ')
n = int(input('Inserire un numero intero: '))
s = ''
for i in range(len(s1)):
   if s2.find(s1[i])>=0 and i-n<=s2.find(s1[i]) and s2.find(s1[i])<=i+n:
       s+=s1[i]
print(s)

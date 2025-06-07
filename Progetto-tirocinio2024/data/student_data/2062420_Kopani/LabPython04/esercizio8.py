s=input('Inserire una stringa: ')
s1=input('Inserire una stringa: ')
while s[-1]!=s1[0]:
	s=s1
	s1=input('Inserire una stringa: ')
print(s,s1)
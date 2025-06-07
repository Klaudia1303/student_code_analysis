s=input('Inserire una stringa con almeno 2 caratteri: ')
n=int(input('Inserire un intero positivo: '))
t=0
for i in range(len(s)):
	if  i+n<=len(s)-1 and s[i]==s[i+n]:
		t+=1	
if t>0:
	print('True')
else:
	print('False')
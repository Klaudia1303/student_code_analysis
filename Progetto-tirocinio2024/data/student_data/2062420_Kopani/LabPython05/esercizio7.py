s=input('Inserire una stringa: ')
t=0
for i in range(len(s)):
	if s.count(s[i])>1:
		t+=1
if t>0:
	print('True')
else:
	print('False')
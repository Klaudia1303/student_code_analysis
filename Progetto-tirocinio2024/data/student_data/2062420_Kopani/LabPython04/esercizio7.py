s=input('Inserire una stringa: ')
c='*'
i=1
while i<len(s):
	if s.count(s[i])>=s.count(s[i-1]):
		c=s[i]
	else:
		c=s[i-1]
	i+=1
print(c)
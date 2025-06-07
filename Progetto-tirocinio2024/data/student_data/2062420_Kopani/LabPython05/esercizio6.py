s=input('Inserire una stringa: ')
max=0
for i in range(len(s)):
	if s.count(s[i])>=2 and s.rfind(s[i])-s.find(s[i])>int(max):
		max=s.rfind(s[i])-s.find(s[i])
print(max)
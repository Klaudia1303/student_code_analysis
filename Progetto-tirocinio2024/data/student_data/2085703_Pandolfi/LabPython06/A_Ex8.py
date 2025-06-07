s1 = input("inserisci una stringa non vuota: ")
s2 = input("inserisci una stringa non vuota: ")
n = int(input("inserisci un intero n: "))

sub = ""
h = 0
l = 0

for x in range(len(s1)):
	l = x-n
	h = x+n
	if x+n > len(s2)-1: 
		h = len(s2)-1
	if x-n < 0: 
		l = 0
	elif x-n > len(s2)-n:
		break
	# print(x, "++++", l, h)
	if s1[x] in s2[l:h]:
		sub = s1[x] + sub

print(sub)
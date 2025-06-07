v1 = 20
v2 = 1

d1 = 0
d2 = 0

for x in range(1000):
	d1 += v1
	d2 += v2
	v2 += 1
	if d1 < d2: 
		print(x)
		break


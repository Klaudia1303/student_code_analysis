import math

def dec_to_oct(dec):
	ott = ""

	while (dec != 0):
		ott = str(dec%8) + ott
		dec = int(dec/8)

	return ott

for x in range(1,11):
	for y in range(1,11):
		print("%02d" % x + "x" + "%02d" % y + "=" + dec_to_oct(x*y))
		#dec_to_oct(x*y)
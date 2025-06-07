l1 = int(input("inserisci primo lato: "))
l2 = int(input("inserisci secondo lato: "))
l3 = int(input("inserisci terzo lato: "))

if l1 and l2 and l3 > 0:
	if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l2+l3):
		if l1 == l2 == l3:
			print("il triangolo e equilatero")
		elif l1 == l2 or l2 == l3 or l1 == l3:
			print("il triangolo è isoscele")
		else:
			print("il triangolo è scaleno")

n = int(input("inserisci un numeratore: "))
d = int(input("inserisci un denominatore: "))

if n<d:
	print("la frazione è propria")
elif n % d == 0:
	print("la frazione è apparente")
elif n>d:
	print("la funzione è impropria")
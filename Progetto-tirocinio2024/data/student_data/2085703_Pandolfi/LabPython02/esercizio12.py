t = int(input("inserisci temperatura: "))
s = input("inserisci C per celsius F per Fahrenheit: ")

if s[0] == "F":
	t = (t - 32)/1.8

if t <= 0:
	print("solido")
elif t > 0 and t < 100:
	print("liquido")
else:
	print("gassoso")
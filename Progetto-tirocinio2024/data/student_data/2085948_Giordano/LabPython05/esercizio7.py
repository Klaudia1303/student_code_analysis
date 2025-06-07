st = input("Inserisci una stringa: ")
x=list(set(st))
y=list(st)
x.sort()
y.sort()
if(x==y):
	print(False)
else:
	print(True)

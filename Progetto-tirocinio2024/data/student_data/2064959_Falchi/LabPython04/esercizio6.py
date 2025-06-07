n1 = int(input("Inserire il primo valore intero: "))
n2 = int(input("Inserire il secondo valore intero: "))

i = 0
Result = 0

while i < abs(n2):
    Result += abs(n1)
    i += 1

if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
	print(n1, "*", n2, "=", Result)
else:
	Result = -Result
	print(n1, "*", n2, "=", Result)

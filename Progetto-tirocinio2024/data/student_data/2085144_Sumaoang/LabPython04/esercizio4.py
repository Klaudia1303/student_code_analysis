s = 0
n = ""
while n != 0:
    n = int(input("Inserire un numero (0 per terminare) :"))
    if n != 0 and n % 3:
        s += n
print(s)

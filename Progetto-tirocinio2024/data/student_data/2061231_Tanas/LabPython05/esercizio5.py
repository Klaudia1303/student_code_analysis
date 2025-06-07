s = input("stringa (min 2 caratteri): ")
while len(s) < 2:
    s = input("stringa (min 2 caratteri): ")

n = int(input("intero positivo: "))
while n <= 0:
    n = int(input("intero positivo: "))

trovate = False
for i in range(0, len(s)-n):
    if s[i] == s[i+n]:
        trovate = True

print(trovate)
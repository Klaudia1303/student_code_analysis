s = input("Inserire stringa: ")

Mem1 = s
Mem2 = None

Corrispondenza_Trovata = False

while not Corrispondenza_Trovata:
    s = input("Inserire stringa: ")
    if Mem1[len(Mem1)-1] == s[len(s)-1]:
        Mem2 = s
        Corrispondenza_Trovata = True

print(Mem1, Mem2)

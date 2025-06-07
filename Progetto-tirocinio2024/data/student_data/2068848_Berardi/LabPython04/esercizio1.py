s = input("Inserisci la stringa: ")
Ns = 1
while s.find("c")<0 or s.find("a")<0:
    Ns += 1
    s = input("Inserisci la stringa: ")
print(Ns)
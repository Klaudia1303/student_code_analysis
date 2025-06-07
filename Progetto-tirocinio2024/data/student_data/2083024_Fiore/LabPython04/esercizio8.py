s1 = input("inserisci una stringa: ")
n = True
while n:
    s2 = input("inserisci una stringa: ")
    if s1[-1] != s2[0]:
        s1 = s2
    else:
        n = False

print(s1, s2)
    

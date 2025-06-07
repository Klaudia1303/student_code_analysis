s = input("Inserisici stringa --> ")
while(s.isalpha()==False or s.islower()==False):
    print(s[0]+s[-1])
    s = input("Inserisici stringa --> ")
print(s[0]+s[-1])

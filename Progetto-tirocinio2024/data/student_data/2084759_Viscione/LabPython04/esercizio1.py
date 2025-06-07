termina=False
n=0
while not termina:
    s=input("Immetti una stringa: ")
    n+=1
    if s.find("a")!=-1 and s.find("c")!=-1:
        termina=True
print(n)

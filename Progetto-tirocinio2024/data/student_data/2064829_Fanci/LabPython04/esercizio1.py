i=0
while True:
    s = input("inserisci stringa: ")
    i+=1
    if s.find("c")!=-1 and s.find("a")!=-1:
        break
print(i)

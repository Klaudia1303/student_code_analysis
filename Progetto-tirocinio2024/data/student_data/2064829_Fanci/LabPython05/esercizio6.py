s = input("inserisci stringa: ")
for i in s:
    sx=s.find(i)
    dx=s.rfind(i)
    if sx!=dx:
        dis=dx-sx
print(dis)


        

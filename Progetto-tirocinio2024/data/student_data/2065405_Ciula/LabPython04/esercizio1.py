p=False
cont=0
while (p==False):
    s=input("Iserisci una stringa: ")
    cont+=1
    if(s.count("c")!=0 and s.count("a")!=0):
        p=True
print(cont)

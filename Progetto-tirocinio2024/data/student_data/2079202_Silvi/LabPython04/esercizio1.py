i=0
v=True
while v:
    s=input("inserire la stringa:")
    if s.find("a")!=-1 and s.find("c")!=-1:
        v=False
        i+=1
    else:
        i+=1
print(i)

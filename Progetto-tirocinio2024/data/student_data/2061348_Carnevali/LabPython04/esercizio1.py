s="totti"
x=0
while s.find("a")==-1 or s.find("c")==-1:
    s=input("inserire una stringa: ")
    x=x+1
    if s.find("a")!=-1 and s.find("c")!=-1:
        print(x)

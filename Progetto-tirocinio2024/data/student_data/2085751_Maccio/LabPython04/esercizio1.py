i=0
var=True
while var:
    s=input("inserire stringa: ")
    if s.count("c")>0 and s.count("a")>0:
        var=False
    i+=1
print(i)

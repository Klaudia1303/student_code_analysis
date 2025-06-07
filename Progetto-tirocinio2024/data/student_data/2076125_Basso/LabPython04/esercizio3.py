
a=1
s=0


while a != "*":
    a=int(a)
    if a < 0:
        s=a+s
        
    a=input("Inserire intero:\t")
    

print(s)

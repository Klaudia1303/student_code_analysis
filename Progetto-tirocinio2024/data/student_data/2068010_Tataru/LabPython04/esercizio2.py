con=True
i=0
while (con==True):
    a=input()
    if(a=="*"):
        break
    if(int(a)>0):
        i+=1
print(i)

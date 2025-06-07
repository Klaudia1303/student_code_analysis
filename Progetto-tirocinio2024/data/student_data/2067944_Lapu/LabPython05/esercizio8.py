x=int(input("inserire base triangolo: "))
f=" "
spaziomeno=0
for i in range (1,x+2,2):
    spazio=f*(x//2-spaziomeno)
    spaziomeno+=1
    carat="*"*i
    print(spazio+carat)

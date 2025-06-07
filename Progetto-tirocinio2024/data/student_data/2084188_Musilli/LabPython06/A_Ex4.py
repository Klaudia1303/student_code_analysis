n1=20; n2=1
for i in range(1,1001):
    d1=n1*i; d2=i*(n2+i)/2
    if d1==d2: break
print("Giorno in cui il secondo(v=1) raggiungerà il primo(v=20), oltre a 0:", i)

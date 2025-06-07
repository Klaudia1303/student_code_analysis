for i in range(1,1000):
    a=i*20
    b=0
    for l in range (i+1):
        b+=l
    if a==b:
        print (i)
        break

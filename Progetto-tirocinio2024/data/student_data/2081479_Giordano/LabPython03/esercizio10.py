finalNumber=int(input('insert x>1: '))
startNumber=2
while startNumber<finalNumber:
    counter=startNumber-1
    factors=0
    while counter>=2:
        if startNumber%counter==0:
            factors+=1
            counter-=1
        elif startNumber%counter!=0:
            counter-=1
    if factors==0:
        print(startNumber)
    startNumber+=1
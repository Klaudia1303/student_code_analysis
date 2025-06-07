n = int(input())
if n >0:
    inizio=1
    while n % inizio == 0:
        print(inizio)
        inizio= inizio+1
    
    print(n)
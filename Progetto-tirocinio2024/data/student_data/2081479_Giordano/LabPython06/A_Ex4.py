days=0
dist2=0
for days in range(1,1000):
    dist1=20*days
    dist2+=days
    if dist2==dist1:
        print(days)
        break

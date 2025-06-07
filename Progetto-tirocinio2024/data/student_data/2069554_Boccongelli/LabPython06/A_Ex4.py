startPos1 = 0
startPos2 = 0
for i in range(1, 1000):
    startPos1 += 20
    startPos2 += i
    if (startPos1 == startPos2):
        print(i)
        break

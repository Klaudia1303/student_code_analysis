

s = input('Inserire una stringa :')

index = 0
occ = 0
egual = False
while(index < len(s)):
    caratt = s[index]
    newOcc = s.count(caratt)
    if(newOcc > occ):
        occ = newOcc
        egual = False
    elif(newOcc == occ):
        egual = True
    index += 1

index = len(s) - 1
while(index >= 0):
    caratt = s[index]
    if(s.count(caratt) == occ):
        print(caratt)
        break
    index -= 1

s = input("inserisci una stringa: ")
numOcc = 1 #numero maggiore di occorrenze consecutive 
numRip = 1 #numero di ripetizioni successive controllato per ogni carattere
for i in range(len(s) -1):
    c = s[i]
    if s[i] == s[i + 1]:
        numRip = numRip + 1
    else:
        numRip = 1
    if numRip >= numOcc:
        numOcc = numRip
        a = c
if numOcc == 1:
    a = s[len(s) -1]
print(a)
print(numOcc)

        

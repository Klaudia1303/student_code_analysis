ac = True
nparole = 0
while ac:
    s = input("Inserire una stringa: ")
    if s.count('a') > 0 and s.count('c') > 0:
        ac = False
    nparole += 1
print(nparole)

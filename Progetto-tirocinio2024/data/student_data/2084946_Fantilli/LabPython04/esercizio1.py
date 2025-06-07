s = input()
i=1
while s.count('a') == 0 or s.count('c') == 0:
    s = input()
    i+=1
    if s.count('a') != 0 and s.count('c') != 0:
        print("numero stringhe inserite: ", i)

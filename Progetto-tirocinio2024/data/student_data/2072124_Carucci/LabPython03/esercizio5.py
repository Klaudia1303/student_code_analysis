stop = False
while not stop:
    s = input('Inserire una stringa: ')
    print(s[0]+s[-1])
    if s.islower() and s.isalpha():
        stop = True
    

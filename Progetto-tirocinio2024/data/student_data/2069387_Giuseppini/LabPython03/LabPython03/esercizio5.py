i=True

while i:
    s=input('scrivi una stringa: ')
    if s.isalpha()and s.islower():
        print(s[0],s[-1])
        i=False
    else:
        print(s[0],s[-1])
        

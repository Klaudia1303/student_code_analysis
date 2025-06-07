n = int(input('inserire un numero maggiore di 1:'))
c = 2
while c <= n:
    primo = True
    divisore = 2
    while divisore < c :
        if c % divisore == 0:
            primo = False
        divisore = divisore + 1
    if primo == True:
        print(c)
    c = c + 1
        
        
        

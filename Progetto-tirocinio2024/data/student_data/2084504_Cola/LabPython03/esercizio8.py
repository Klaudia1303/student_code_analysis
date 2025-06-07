s=input('scrivere una frase: ')
b=s[::-1]
while s!=b:
    print('non palindroma')
    s=input('inserire una stringa palindroma: ')
    b=s[::-1]
print('stringa palindroma di lunghezza',len(s))
    
    
    



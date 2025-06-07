#Riconosci una parola palindroma e di la sua lunghezza

s = input('Scrivi una parola palindroma = ')
b = 0

while s[0] != s[-1]:
    print('non palindroma, inserire una stringa palindroma')
    s = input()


while s[0] == s[-1] and len(s) != 1:
    s = s[1:len(s)-1]
    b = b+1
    while s[0] != s[-1] and len(s) != 1:
        print('non palindroma, inserire una stringa palindroma')
        b = 0
        s = input()

if len(s) == 1:
    print('stringa palindroma di lunghezza',b*2+1)
    

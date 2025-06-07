#Trova più di 2 volte un carattere c in una stringa s

c = input('Scrivi un carattere = ')
s = input('Scrivi una stringa = ')

while s.count(c) <= 2:
    s = input('Ancora = ')

if s.count(c) > 2:
    print(s.count(c))



        

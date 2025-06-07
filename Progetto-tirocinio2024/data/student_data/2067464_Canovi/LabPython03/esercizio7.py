c = input("inserisci un carattere: ")
b = 0
while b <= 1:
    s = input("inserisci una stringa: ")
    a = 0
    
    while a < len(s):
        if s[a] == c:
            b = b + 1
        a = a + 1
print(b)
            

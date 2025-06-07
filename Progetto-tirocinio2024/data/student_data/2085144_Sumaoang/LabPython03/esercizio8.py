i = 0

while i==0:
    s = input("Inserire una stringa palindroma:")
    if s[0:] == s[::-1]:
            print("stringa palindroma di lunghezza", len(s))
            i = i+1
    elif s[0:] != s[::-1]:
            print("non palindroma, inserire una stringa palindroma")
        
        
        

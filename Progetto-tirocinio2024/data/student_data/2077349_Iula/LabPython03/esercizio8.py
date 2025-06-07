s=input("Inserire una stringa palindroma: ")    
while s[::-1]!=s:
    s=input("non palindroma, inserire una stringa palindroma: ")
if s[::-1]==s:
    print("stringa palindroma di lunghezza ",len(s))
    

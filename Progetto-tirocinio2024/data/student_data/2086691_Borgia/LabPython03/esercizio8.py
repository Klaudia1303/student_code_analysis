s=input("Inserire una stringa palindroma: ")
while s[0:]!=s[::-1]:
    s=input("non palindroma, inserire una stringa palindroma: ")
print("stringa palindroma di lunghezza",len(s))
    

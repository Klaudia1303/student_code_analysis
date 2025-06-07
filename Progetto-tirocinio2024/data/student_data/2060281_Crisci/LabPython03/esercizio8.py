s=str(input("Inserire una stringa palindroma: "))
while(s[:]!=s[::-1]):
    s=str(input("stringa non palindroma, inserire una stringa palindroma: "))
print("stringa palindroma di lunghezza "+ str(len(s)))

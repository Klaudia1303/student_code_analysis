s=input("inserire una stringa palindroma: ")
while s!=s[::-1]:
    s=input("non palindroma, inserire una stringa palindroma:")
    if s==s[::-1]:
        print("stringa palindroma di lunghezza",len(s))

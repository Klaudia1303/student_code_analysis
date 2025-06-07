s = input("stringa: ")
i=0
while s[i] != s[(len(s)-i-1)]:
    i+=1
    print("non palindroma, inserire una stringa palindroma: ")
    s = input("stringa: ")
if s[i] == s[(len(s)-i-1)]:
    print("stringa palindroma di lunghezza", len(s))

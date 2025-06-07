s = input("Inserire una stringa: ")
ultimo = s[-1]
primo=""
while ultimo!=primo:
    ultimo = s[-1]
    s1=s
    s = input("Inserire una stringa: ")
    primo=s[0]
print(s1,"",s)
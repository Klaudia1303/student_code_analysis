s="Totti10"
while s.isalpha()==False or s.islower()==False:
    s=input("inserire una stringa: ")
    n=len(s)-1
    print(s[0],s[n])

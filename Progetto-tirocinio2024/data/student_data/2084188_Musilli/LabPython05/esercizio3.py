s1=input("Inserire la prima stringa: ")
s2=input("Inserire la seconda stringa: ")
s=""
for c1 in s1:
    b=True
    for c2 in s2:
        if c1==c2:  b=False; break
    if b:   s+=c1
print("\n\t\tStringhe iniziali:\n\t-",s1,"\n\t-",s2,"\n\nStringa finale:",s)

s=input("Inserire la prima stringa:")
m=input("Inserire la seconda stringa:")
parola=""
for i in s:
    if m.count(i)==0:
        parola=parola+i
print(parola)

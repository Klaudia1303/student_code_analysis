s1=input("inserire una stringa: ")
s2=input("inserire una stringa: ")
r=""
p=(0,0)
if s1=="" or s2=="":
    print("input non valido")
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        if s1[i:j] in s2:
            if j-i>p[1]-p[0]:
                p=(i,j)
        else:
            break
print(s1[p[0]:p[1]])

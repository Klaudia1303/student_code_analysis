s1=input('inserire la prima stringa:')
s2=input('inserire la seconda stringa:')
x='' #stringa più lunga
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]!=s2[j]:
            break
        else:
            i+=1
            x+=s2[j]
print(x)

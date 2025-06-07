s = input("")
if len(s)>0:
    pass
else:
    exit
stri=""
num =0
occ=0
for i in range(len(s)):
    num = s.count(s[i])
    if num>= occ:
        stri =s[i]
        occ=num
print(stri, num)

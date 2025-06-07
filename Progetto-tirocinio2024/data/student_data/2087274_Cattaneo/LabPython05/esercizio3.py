s1=input('stringa=')
s2=input('stringa=')
s=''
for c in s1:
    if not (c in s2):
        s+=c
print(s)

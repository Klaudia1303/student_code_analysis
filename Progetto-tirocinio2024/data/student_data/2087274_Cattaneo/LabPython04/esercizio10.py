s=input('s=')
s1=input('s=')
s2=input('s=')
while len(s)+len(s1)!=len(s2):
    s=s1
    s1=s2
    s2=input('s=')
print(s,s1,s2)

s1 = input('inserire una stringa')
s2 = input('inserire una stringa')
dist = int(input('inserire un intero positivo'))
a=""
l1= len(s1)
l2= len(s2)
for i in range (l1):
    if(s1[i] in s2 and (s2.find(s1[i])<=i+2 and s2.find(s1[i])>=i-2)):
        a+=s1[i]
print(a)

    
    

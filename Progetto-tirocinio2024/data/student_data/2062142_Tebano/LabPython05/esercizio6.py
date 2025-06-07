s=str(input())
mas=0
for i in range(0,len(s)-1):
    lett=s[i]
    n=abs(s.find(lett)-(s.rfind(lett)))
    
    if n>mas:
        mas=n
print(mas)        

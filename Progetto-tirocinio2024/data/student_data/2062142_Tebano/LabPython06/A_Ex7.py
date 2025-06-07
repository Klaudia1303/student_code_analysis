s1=str(input('s1='))
s2=str(input('s2='))
s=''
m=0
for i in range(len(s1)-1,0,-1):
    for j in range(0,len(s1)-i):
        s=s1[j:j+i+1]
        if s in s2 and len(s)>=m:
            m=len(s)
            print(s)
            break   
  

        

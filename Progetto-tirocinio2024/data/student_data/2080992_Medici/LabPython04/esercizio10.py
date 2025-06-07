s=str(input('inserire una stringa: '))
s1=s
l1=len(s1)
s=str(input('inserire una stringa: '))
s2=s
l2=len(s2)
i=0
while i!=1:
    s=str(input('inserire una stringa: '))
    s3=s
    l3=len(s)
    if l3==l1+l2:
          print(s1,s2,s3)
          i=1
    else:
        s1=s2
        s2=s3
        l1=l2
        l2=l3
            
        
        
        
    
    
   
        
    

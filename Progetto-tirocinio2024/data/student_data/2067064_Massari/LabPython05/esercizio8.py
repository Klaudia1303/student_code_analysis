s=int(input('inserire la base del triangolo isoscele: '))
spazi=int((s-1)/2)
if s>2 and s%2==1:
    for i in range(1,s+1,2):
        print(' '*spazi,'*'*i)
        spazi-=1
    
   

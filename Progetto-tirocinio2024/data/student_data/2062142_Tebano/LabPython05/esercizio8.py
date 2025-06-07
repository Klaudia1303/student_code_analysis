finish=False
while finish==False:
    n=int(input('inserisci base triangolo isoscele(n dispari >3)'))
    for i in range(1,n+1,2):
        print(' '*((n-i)//2),'*'*i,' '*((n-i)//2))
    o=input('finish? Yes or No')
    if o.lower()=='yes':
              finish=True
              
              
        
              
          
    

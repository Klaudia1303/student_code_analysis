s=input('inserire stringa: ')
n_s=1
c=True

while c==True:
    if s.find('a')!=-1 and s.find('c')!=-1:
        print(n_s)
        c=False
    else:
        s=input('inserire stringa: ')
        n_s+=1
        

n=int(input('Base triangolo '))
for i in range(1,n+1,2):
    if n-1!=0:
        print(' '*int(((n-1)/2)-1),'*'*i,' '*int((((n-1)/2))-1))
    else:
        print('*'*i)
    n=n-2

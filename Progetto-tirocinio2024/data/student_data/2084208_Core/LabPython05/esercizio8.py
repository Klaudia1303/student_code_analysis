n=int(input('Inserire la base di un triangolo isoscele: '))
blank=' '
toglispazio=0
for i in range(1,n+1,2):
    spazio=blank*(n//2-toglispazio)
    segno=i*'*'
    print(str(spazio)+str(segno))
    toglispazio+=1


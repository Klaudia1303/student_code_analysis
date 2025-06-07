start=2
end=int(input('please type a number greater than 2: '))
if end>=2:
    for num in range(start,end+1):
        if num%2==0:
            print (num,end='\n\n')
else:
    while end<2:
        print('the number must be greater than 2.')
        end=int(input('please type a number greater than 2: '))
            

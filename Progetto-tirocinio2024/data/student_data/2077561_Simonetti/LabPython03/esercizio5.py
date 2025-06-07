i=input('please type a word: ')

while i.islower()==False or i.isalpha()==False:
    print(i[0]+i[-1])
    i=input('please type a word: ')

if i.islower()==True and i.isalpha()==True:
    print(i[0]+i[-1])


    

    

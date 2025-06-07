firstString=input('please enter a word: ')
secondString=input('please enter another word: ')
while len(firstString)!=len(secondString):
    print('The two strings must be of equal number of characters.',end='')
    firstString=input(' Please enter a word: ')
    secondString=input('Please enter the second word: ')
if len(firstString)==len(secondString):
    newS=''
    for i in range (0,len(firstString)):
        newS=newS+(firstString[i]+secondString[i])
    print(newS)

        

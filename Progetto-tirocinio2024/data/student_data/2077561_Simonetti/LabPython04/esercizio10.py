strSum=0
found=False
string=input('please enter a word: ')
string2=input('please enter another word: ')
string3=input('please enter the last word. If the lenght of this word is equal to the lenght of the past two i\'ll terminate: ')
if string!='' and string2!='' and string3!='':
    while not found:
        strSum=len(string)+len(string2)
        if len(string3)==strSum:
            found=True
        else:
            string=string2
            string2=string3
            string3=input('please try again, if the lenght of this word is equal to the lenght of the two previous combined i\'ll terminate:')
            while string3=='':
                print('please enter anything before pressing \'enter\'')
                string3=input('please try again, if the lenght of this word is equal to the lenght of the two previous combined i\'ll terminate:')
            strSum=len(string)+len(string2)
            
    print(string,string2,string3)
else: print('please enter anything before pressing \'enter\'')

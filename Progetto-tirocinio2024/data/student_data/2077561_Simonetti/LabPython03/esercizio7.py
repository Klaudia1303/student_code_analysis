characterCount=input('please type the character you want to find: ')
end=False
while end==False:
    s=input('please type a word or sentence: ')
    if characterCount in s:
        if s.count(characterCount)>2:
            print (s.count(characterCount))
            end=True
        
            
        

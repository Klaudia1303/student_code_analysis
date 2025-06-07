character=input('insert character: ')
counter=0
while counter<=2:
    word=input('insert a word: ')
    scan=0
    while scan<=len(word):
        if character==word[scan:scan+1]:
            counter+=1
            scan+=1
        elif character!=word[scan:scan+1]:
            scan+=1
    if counter>2:
        print(counter)
        exit()
    else:
        counter=0
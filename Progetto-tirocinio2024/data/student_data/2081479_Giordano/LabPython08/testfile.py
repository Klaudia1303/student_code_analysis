def A_Ex8(l):
    finalSet=set()
    counter=0
    for setScan in l:
        for item in setScan:
            finalSet.add(item)
            print(finalSet)
    for setScan in l:
        for item in setScan: 
            print(item)
            counter=0
            while counter<len(l):
                if l[counter]==setScan:
                    counter+=1
                    continue
                elif item in l[counter] and item in finalSet:
                    finalSet.remove(item)
                    counter+=1
                else:
                    counter+=1
    print(finalSet)
A_Ex8([{3,2,90},{2,87,23},{2,23,3}])
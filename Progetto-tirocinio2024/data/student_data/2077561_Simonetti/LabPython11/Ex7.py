def Ex7(file):
    fin=open(file,encoding='UTF-8')
    finR=fin.read()
    category=['altri','domestici','invalidi']
    pattern=r'\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b'
    dictionary={i:0 for i in category}
    finditer=re.finditer(pattern,finR)
    
    for i in finditer:
        if int(i.group(1))==192 and int(i.group(2))==168 and int(i.group(3))<=255 and int(i.group(4))<=255:
            dictionary[category[1]]+=1    
        elif int(i.group(1))<=255 and int(i.group(2))<=255 and int(i.group(3))<=255 and int(i.group(4))<=255:
            dictionary[category[0]]+=1
        else:
            dictionary[category[2]]+=1
            
    if sum(dictionary.values())!=len(finR.split('\n')):
        dictionary[category[2]]=len(finR.split('\n'))-sum(dictionary.values())
        
    return dictionary

    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
    counter_test_positivi += tester_fun(Ex7, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
    counter_test_positivi += tester_fun(Ex7, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})
    
    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

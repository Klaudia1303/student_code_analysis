def Ex7(file):
    f=open(file, encoding='UTF-8')
    testo=f.readlines()
    f.close()
    d={'invalidi': 0, 'domestici': 0, 'altri': 0}
    patt=r'(\d+)\.(\d+)\.(\d+)\.(\d+)'
    pattdom=r'192\.168\.\d+\.\d+'
    validi=[]
    for elem in testo:
        elem=elem.strip()
        ris=re.match(patt, elem)
        flag=0
        for i in range (1,5):
            if not ris.group(i).isdecimal() or not 0<=int(ris.group(i))<=255 or len(ris.group(i))>3:
                d['invalidi']+=1
                flag=1
                break
        if flag==0:
            validi.append(elem)
    for ip in validi:
        if re.match(pattdom, ip):
            d['domestici']+=1
        else:
            d['altri']+=1
    return d
    
    
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

def Ex7(file):
    fin=open(file,encoding="UTF8").readlines()
    diz={}
    diz["domestici"]=0
    diz["altri"]=0
    diz["invalidi"]=0
    pattern=r"\b(\d?\d?\d)\.(\d?\d?\d)\.(\d?\d?\d)\.(\d?\d?\d)\b"
    for elem in fin:
        ip=re.search(pattern,elem)
        if ip:
            if int(ip.group(1))<=255 and int(ip.group(2))<=255 and int(ip.group(3))<=255 and int(ip.group(4))<=255:
                if ip.group(1)=="192" and ip.group(2)=="168":
                    diz['domestici']+=1
                else:
                    diz["altri"]+=1
            else:
                diz["invalidi"]+=1
        else:
            diz["invalidi"]+=1
    return diz
    
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

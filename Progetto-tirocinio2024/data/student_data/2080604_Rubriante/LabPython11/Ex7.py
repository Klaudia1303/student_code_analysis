def Ex7(file):
    f=open(file,encoding="UTF-8")
    validi=r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    domestici=r"\b192\.168\.(?:[0-9]{1,3}\.)[0-9]{1,3}\b"
    diz={'invalidi': 0, 'domestici': 0, 'altri': 0}
    for riga in f:
        lipu=riga.strip().split(".")
        riga=riga.strip()
        if re.findall(domestici,riga) and all(0<=int(i)<=255 for i in lipu):
            diz["domestici"]+=1
        elif re.findall(validi,riga) and all(0<=int(i)<=255 for i in lipu):
            diz["altri"]+=1
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

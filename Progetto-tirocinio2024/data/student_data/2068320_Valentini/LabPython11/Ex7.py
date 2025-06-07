def Ex7(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""    
    l = open(file)
    r = l.readlines()
    invalidi = 0
    domestici = 0
    altri = 0
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    pattern2 = r"\b192.168\b"
    dizionario={}
    for i in range(len(r)):
        indirizzo = str(r[i]).strip()
        cerca = re.match(pattern, indirizzo)
        if cerca:
            ip = indirizzo.split(".")
            conta = 0
            for k in range(len(ip)):
                numero = int(ip[k])
                if numero > -1 and numero < 256:
                    conta += 1
                    if conta == 4:
                        conta = 0
                        cerca2 = re.match(pattern2, indirizzo)
                        if cerca2:
                            domestici+=1
                        else:
                            altri+=1
                else:
                    conta = 0
                    invalidi += 1
                
        else:
            invalidi += 1
    dizionario["invalidi"] = invalidi
    dizionario["domestici"] = domestici
    dizionario["altri"] = altri
    return(dizionario)
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

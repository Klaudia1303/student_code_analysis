def Ex7(file):

    f=open(file,encoding="utf")
    d={"invalidi":0, "domestici": 0, "altri": 0}
    sv=[]
    for elem in f:
        elem=elem.strip().split("\n")
        sv.append(elem)
    for i in sv:
        for e in i:
            sol=e.strip().split(".")
            if (sol[0]=='192' and sol[1]=='168') and (int(sol[2])>=0 and int(sol[2])<=255) and (int(sol[3])>=0 and int(sol[3])<=255) and (len(sol[2])<=3 and len(sol[3])<=3):
                d['domestici'] += 1
            elif (int(sol[0])>=0 and int(sol[0])<=255) and (int(sol[1])>=0 and int(sol[1])<=255) and (int(sol[2])>=0 and int(sol[2])<=255) and (int(sol[3])>=0 and int(sol[3])<=255) and (len(sol[0])<=3 and len(sol[1])<=3 and len(sol[2])<=3 and len(sol[3])<=3):
                d['altri'] += 1
            else:
                d['invalidi'] += 1
    f.close()
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

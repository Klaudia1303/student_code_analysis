def Ex7(file):
    diz={'invalidi':0, 'domestici':0, 'altri':0}
    f=open(file)
    righe=f.readlines()
    for i in range(len(righe)):
        indirizzo=righe[i].strip().split('.')
        i1=len(indirizzo[1])
        i2=len(indirizzo[2])
        i3=len(indirizzo[3])
        i4=len(indirizzo[0])
        if 0<=int(indirizzo[2])<256 and 0<=int(indirizzo[3])<256 and i4<4 and i3<4 and i1<4 and i2<4:
            if int(indirizzo[0])==192 and int(indirizzo[1])==168:
                n=diz.get('domestici')
                diz['domestici']=n+1
            elif 0<=int(indirizzo[0])<256 and 0<=int(indirizzo[1])<256:
                n=diz.get('altri')
                diz['altri']=n+1
            else:
                n=diz.get('invalidi')
                diz['invalidi']=n+1
        else:
            n=diz.get('invalidi')
            diz['invalidi']=n+1
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

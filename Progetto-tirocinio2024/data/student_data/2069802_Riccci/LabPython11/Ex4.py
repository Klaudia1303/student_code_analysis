def Ex4(file):
    f=open(file,encoding="UTF-8")
    d={}
    campi=f.readline()
    campi=campi.strip().split(',')
    riga=f.readline()
    while len(riga)>0:
        riga=riga.strip().split(',')
        oggetto=riga[0]
        if oggetto not in d:
            d[oggetto]=[riga[1]]
        if len(d[oggetto])>1:
            lista=d[oggetto]
            if lista[1]==riga[1]:
                el_rimosso=d[oggetto].pop()
                d[oggetto].append(riga[2])
        elif len(d[oggetto])==1:
            d[oggetto].append(riga[2])
        riga=f.readline()
    f.close()
    return d
    
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex4, ["eredita1.csv"] , {'Anello_di_smeraldi': ['Maria', 'Giorgia'], 'Anello': ['Silvia', 'Paolo']})
    counter_test_positivi += tester_fun(Ex4, ["eredita2.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita3.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Anna', 'Sergio']})
    counter_test_positivi += tester_fun(Ex4, ["eredita4.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Giorgio'], 'Vaso': ['Anna', 'Anna']})
    counter_test_positivi += tester_fun(Ex4, ["eredita5.csv"] , {'Anello_di_smeraldi': ['Marco', 'Giorgio'], 'Anello': ['Silvia', 'Sergio'], 'Vaso': ['Sergio', 'Anna']})

    print('La funzione',Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

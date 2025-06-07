def Ex4(file):
    keys = []
    d = {}

    fin = open(file,encoding = 'UTF-8')
    next(fin)
    for riga in fin :
        riga = riga.strip().split(',')
        if riga[0] not in keys :
            keys.append(riga[0])

    fin.close()
    fin = open(file,encoding = 'UTF-8')
    next(fin)
    righe = fin.readlines()
    for key in keys :
        valore = []
        for riga in righe:
            riga = riga.strip().split(',')
            if valore == [] and key == riga[0] :
                valore.append(riga[1])
                valore.append(riga[2])
            elif valore != [] and key == riga[0] and valore[1] == riga[1] :
                valore.remove(valore[1])
                valore.append(riga[2])
        d[key] = valore
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

def A_Ex8(file):
    fin=open(file,encoding="utf-8")
    relazione=[]
    risultato={}
    for riga in fin:
        relazione.append(riga.strip().split(","))
    relazione.remove(relazione[0])
    for rapporto in relazione:
        if rapporto[2].lower()=="amici":
            if rapporto[0] not in risultato:
                risultato[rapporto[0]]=[]
            if rapporto[1] not in risultato:
                risultato[rapporto[1]]=[]
            if rapporto [1] not in risultato[rapporto[0]]:
                risultato[rapporto[0]].append(rapporto[1])
            if rapporto[0] not in risultato[rapporto[1]]:
                risultato[rapporto[1]].append(rapporto[0])
        if rapporto[2].lower()=="nemici":
            if rapporto[0] not in risultato:
                risultato[rapporto[0]]=[]
            if rapporto[1] not in risultato:
                risultato[rapporto[1]]=[]
            if rapporto[1] in risultato[rapporto[0]]:
                risultato[rapporto[0]].remove(rapporto[1])
            if rapporto[0] in risultato[rapporto[1]]:
                risultato[rapporto[1]].remove(rapporto[0])
    for chiave in risultato:
        risultato[chiave].sort()
    return risultato
            
        
    
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["amici1.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici2.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria'], 'Maria': ['Anna'], 'Paola': [], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici3.csv"] , {'Paolo': ['Marco'], 'Marco': ['Paolo'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna'], 'Giorgio': []})
    counter_test_positivi += tester_fun(A_Ex8, ["amici4.csv"] , {'Marco': ['Giorgio', 'Paolo'], 'Giorgio': ['Marco'], 'Paolo': ['Marco'], 'Anna': ['Maria', 'Paola'], 'Maria': ['Anna'], 'Paola': ['Anna']})
    counter_test_positivi += tester_fun(A_Ex8, ["amici5.csv"] , {'Marco': [], 'Giorgio': [], 'Paola': [], 'Anna': []})

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

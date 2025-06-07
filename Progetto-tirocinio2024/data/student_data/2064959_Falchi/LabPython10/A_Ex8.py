def A_Ex8(fileName):
    d = dict()

    with open(fileName, "r", encoding="UTF-8") as file:
        titoli = file.readline().strip().split(",")

        for rigaNonFormattata in file.readlines():
            riga = rigaNonFormattata.strip().split(",")
            
            print(riga)

            amico1 = riga[0]
            amico2 = riga[1]
            relazione = riga[2]

            if amico1 not in d:
                d[amico1] = list()
            if amico2 not in d:
                d[amico2] = list()
    
            if relazione == "amici":
                if amico2 not in d[amico1]:
                    d[amico1].append(amico2)
                if amico1 not in d[amico2]:
                    d[amico2].append(amico1)
            elif relazione == "nemici":
                if amico2 in d[amico1]:
                    d[amico1].remove(amico2)
                if amico1 in d[amico2]:
                    d[amico2].remove(amico1)
            
            for chiave in d: #riordina le liste
                d[chiave].sort()

        return d

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

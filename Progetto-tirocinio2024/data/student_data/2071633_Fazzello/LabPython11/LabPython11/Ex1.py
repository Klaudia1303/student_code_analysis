## scrivere la funzione Python che, preso in ingresso il nome di un file di testo, calcoli, usando le 
##espressioni regolari, quante sono le sequenze non sovrapposte di 2 parole consecutive aventi la seguente 
##proprietà: 
##“La due parole sono composte da almeno due caratteri ed hanno a stessa lettera iniziale e 
##la stessa lettera finale, ignorando la distinzione fra maiuscole e minuscole.”
##Ad esempio, prendendo come input il file contenente il seguente testo: 
##tanto va Aldino annaspando in giro che era andato al bar
##la funzione deve restituire come risultato 1

def Ex1(file):
    f = open(file,encoding="UTF-8")
    s = f.read()
    f.close()
    pattern = r'\b(\w)\w*(\w)\b\W*\b\1\w*\2\b'
    mn = re.finditer(pattern,s,re.IGNORECASE)
    c = 0
    for m in mn:
        print(m.group())
        c += 1
    return c

###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, ["file1_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex1, ["file1_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex1, ["file1_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_4.txt"] , 3)
    counter_test_positivi += tester_fun(Ex1, ["file1_5.txt"] , 5)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

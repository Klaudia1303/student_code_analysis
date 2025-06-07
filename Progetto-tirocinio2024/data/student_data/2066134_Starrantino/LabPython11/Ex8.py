def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    data = [line.strip().replace(' ', '') for line in open(file).readlines()]
    pattern = r'\b[A-Z]{6}(\d{2})([A-Z])(\d{2})[A-Z]\d{3}[A-Z]\b'
    months = 'ABCDEHLMPRST'
    out: list[str] = []
    for code in data:
        m = re.match(pattern, code)
        if m:
            year, month, day = m.groups()
            if month not in months:
                out.append('Mese errato')
                continue
            monthIndex = months.index(month) + 1
            month = f'0{monthIndex}' if monthIndex < 10 else monthIndex
            day = int(day)
            day = day-40 if day > 40 else day
            if ((day < 1 or day > 31) or (month == '02' and day > 28)):
                out.append('Giorno errato')
                continue
            day = f'0{day}' if day < 10 else day
            year = int(year)
            year = f'20{year}' if year <= 20 else f'19{year}'
            out.append(f'{day}/{month}/{year}')
        else: out.append('Codice errato')
    return out
        
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

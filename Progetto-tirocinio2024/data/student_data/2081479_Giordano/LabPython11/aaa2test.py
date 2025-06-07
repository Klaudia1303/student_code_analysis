import re 
def Ex4(file):
 with open(file, encoding='UTF-8') as file:
        txt=file.read()
        pattern=r'.*?\b(\w+),(\w+),.*?\1,\2,(\w+)'
        result=re.findall(pattern,txt, flags=re.IGNORECASE|re.DOTALL)
        print(result)
Ex4('eredita2.csv')

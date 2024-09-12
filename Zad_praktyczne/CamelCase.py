import sys

def countSigns(tab):
    return tab.count("_") + tab.count("-")

def changeToUpper(tab):
    for i in range(0,len(tab)-countSigns(tab)):
        if tab[i] == "-" or tab[i] == "_":
            tab.pop(i)
            tab[i] = tab[i].upper()
    return tab       

text = sys.argv[1]
if any(map(str.isupper, text)):
    print("Upper letter")
else:
    tab = list(text)
    changeToUpper(tab)
    text = ''.join(map(str,tab))
    print(text)


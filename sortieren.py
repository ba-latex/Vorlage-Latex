import re
acros = []
inhalt = []
zeilennummer = 0
minimum = 0
with open("Latex/inhalt/Abkürzungen.tex", "r+", encoding="utf-8") as datei:
    for zeile in datei:
        zeilennummer += 1
        inhalt.append([zeilennummer, zeile.replace("\n", "")])
        if "\\acro" in zeile:
            if minimum == 0:
                minimum = zeilennummer
            eins = zeile.split("}")[0].split("{")[1]
            acros.append([eins, zeilennummer, zeile.replace("\n", "")])
            #print(eins)
            #print(zwei)
    #print(acros)
    liste = sorted(acros, key=(lambda x: x[0].upper()), reverse=False)
    #print(liste)
    #print(inhalt)
with open("Latex/inhalt/Abkürzung_sortiert.tex", "w+", encoding="utf-8") as neu:
    i = 0
    anzahl = len(liste)
    #print(anzahl)
    for zeile in inhalt: 
        if zeile[0] == minimum:
            print(liste[i][2], file=neu)
            minimum += 1
            i += 1
            if i >= anzahl:
                minimum = 30
        else:
            print(zeile[1], file=neu)

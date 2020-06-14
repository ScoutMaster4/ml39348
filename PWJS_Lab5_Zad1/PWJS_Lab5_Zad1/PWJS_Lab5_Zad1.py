# Łukasz Maćkiewicz
# 39348
# 31B
# PWJS Lab5 Python
# Zadanie w wariancie na 4.0
import os, sys
if len(sys.argv) < 2:
	print ("nie podano argumentu")
	sys.exit(0);
else:
    nazwaSciezki = sys.argv[1]
    print("\n\t| < Wyszukiwanie duplikatów plików w katalogu '", nazwaSciezki, '\' > |\n')
    listaPlikow = os.listdir(nazwaSciezki)

    kontenerPlikow = list()
    for plikZlisty in listaPlikow:
        sciezka = os.path.join(nazwaSciezki,plikZlisty)
        if os.path.isdir(sciezka):
            continue
        else:
            filesize = os.stat(sciezka).st_size
            file_contain = open(sciezka, errors='ignore').read()
            trojka = [plikZlisty, filesize, file_contain]
            kontenerPlikow.append(trojka)

    slownikDuplikatow = dict()
    for trojka in kontenerPlikow:
        dwojka = os.path.join(str(trojka[1]),trojka[2])
        if slownikDuplikatow.__contains__(dwojka):
                slownikDuplikatow[dwojka].append(trojka[0])
        else:
            slownikDuplikatow[dwojka]=list()
            slownikDuplikatow[dwojka].append(trojka[0])

    lacznyRozmiar = 0
    print ("\t Lista duplikatów: ")
    print("/////////////////////////////////////\n")
    for dwojka in slownikDuplikatow:
        temp = dwojka
        dwojkaRozdzielona = temp.split("\\",1)
        rozmiar = dwojkaRozdzielona[0]
        lacznyRozmiar += int(rozmiar)
        if len(slownikDuplikatow[dwojka])>1: #jezeli duplikaty istnieja
            for items in slownikDuplikatow[dwojka]:
                print(">\t"+items+" ("+rozmiar+"b)")
            print("\n/////////////////////////////////////\n")

    print(" rozmiar plików sprawdzanego folderu: (rozmiar: ", lacznyRozmiar, "b )\n")
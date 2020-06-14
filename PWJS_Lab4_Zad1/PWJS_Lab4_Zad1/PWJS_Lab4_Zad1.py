# Łukasz Maćkiewicz
# 39348
# 31B
# PWJS Lab4 Python
# Zadanie na ocenę 3.0 (za 1 punkt)
from string import ascii_uppercase
from operator import itemgetter
from collections import defaultdict
import textwrap, fileinput, collections
import sys
import string

if len(sys.argv) < 2:
	print ("nie podano argumentu")
	sys.exit(0);
else:
    file = open(sys.argv[1])
    zawartosc = file.read()

litery = ascii_uppercase
data = len(zawartosc)
licznik = 0
slownik = defaultdict(int)

for i in zawartosc:
    for j in i:
        if j.upper() in litery:
            slownik[j.upper()] += 1
            licznik += 1

sorter = sorted(slownik.items(), key=itemgetter(1),reverse=True)
slownikPosortowany = dict(sorter)

for k in slownikPosortowany:
    procent = round(((float(slownikPosortowany[k]) / float(licznik)) * 100), 3)
    print (k, "=",slownikPosortowany[k],"x (",procent,"%)")

print ('\n', "Suma liter: ", licznik, '\n')
file.close()
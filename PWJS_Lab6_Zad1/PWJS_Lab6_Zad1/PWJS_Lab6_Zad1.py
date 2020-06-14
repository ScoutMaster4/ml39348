# Łukasz Maćkiewicz
# 39348
# 31B
# PWJS Lab6 Python
# Zadanie na ocenę 3.0 (Zad 1 Perl namiastka 'ls')
import os
import sys

if len(sys.argv) < 2:
	lista = os.listdir(os.getcwd())
	sorted_list = sorted(lista)
	for i in sorted_list:
		print (i)
else:
	lista = os.listdir(sys.argv[1])
	sorted_list = sorted(lista)
	for i in sorted_list:
		print (i)
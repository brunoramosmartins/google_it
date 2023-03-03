#! /usr/bin/env python3
import os
import requests

for file in os.listdir("supplier-data/descriptions"):
    filename = 'supplier-data/descriptions/'+file
    arquivo = open(filename, "r")
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.rstrip())

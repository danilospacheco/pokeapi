import requests
import os
import csv
import pandas as pd
import argparse
#import pypokedex

filename = 'pokeapi.csv'

# Abrindo CSV para adicionar as informações
with open('pokeapi.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ID', 'Nome', 'Tipo', 'Habilidades', 'Estatistica']) 


os.system('clear')


def pegar_habilidades(poke):
    #print('#########################')
    #print(f'Habilidades do {pokemon} é:')
    print("HABILIDADES DO ", poke["name"])
    #print()
    for i in poke['abilities']:
        print(i['ability']['name'])
    print()
    #return pegar_habilidades

def info_basica(poke):
    #print(f'Tipo de Pokemon:  {pokemon}')
    print(poke["name"], 'É UM TIPO DE POKEMON:')
    for i in poke['types']:
        print(i['type']['name'])
    print()

def estatistica(poke):
    #print('#########################')
    #print(f'estatisticas: {pokemon}')
    print("ESTATISTICA DO ",poke["name"])
    #print()
    for i in poke['stats']:
        print(i['stat']['name'])
    print()

def Id(poke):
    #print('#########################')
    print("NUMERO "f'ID')
    print(poke["id"])
    print()

def Nome(poke):
    #print('#########################')
    print("NOME DO POKEMON: ")
    print(poke["name"])
    print()

    #print(poke["id"])
    #for i in poke['stats']:
       # print(i['stat']['name'])
    #print()
    
def main():
    global pokemon
    pokemon = str(input('Pokemon : '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    os.system('clear') # limpar linha pesquisa
    res=requests.get(api)
    poke=res.json()
    print('### CONSULTANDO INFORMAÇÕES ### ')
    print()
    #print("NOME DO POKEMON ",poke["name"])
    #print()
    Nome(poke)
    Id(poke)
    info_basica(poke)
    pegar_habilidades(poke)
    estatistica(poke)


    #print("ID.: ",poke["id"])

#    if requests.status_code != 200:
#        print('Pokemon não encontrado')
#        exit()


if __name__ == '__main__':

    main()
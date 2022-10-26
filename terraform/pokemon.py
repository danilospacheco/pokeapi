import requests
import os
import csv
import pandas as pd
import argparse

#import pypokedex

filename = 'pokedex.csv'

# Abrindo CSV para adicionar as informações
with open('pokedex.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['ID', 'Nome', 'Tipo', 'Habilidades', 'Estatistica']) # escreve tres strings no csv
    
os.system('clear')


filename = 'pokedex.csv'
csv_data = [] #[['bulbasaur', 'overgrow, chlorophyll', 'grass, poison']]


def pegar_habilidades(poke):
    print('#########################')
    print(f'Habilidades do {pokemon}')
    print()
    for i in poke['abilities']:
        print(i['ability']['name'])
    #return pegar_habilidades

def info_basica(poke):
    print('#########################')
    print('CONSULTANDO DADOS DOS POKEMONS')
    print(poke["name"])
    print('#########################')
    print()
    print(f'Tipo do Pokemon:  {pokemon}')

    for i in poke['types']:
        print(i['type']['name'])

def estatistica(poke):
    print('#########################')
    print(f'estatistica: {pokemon}')
    print()
    for i in poke['stats']:
        print(i['stat']['name'])

def Id(poke):
    print('#########################')
    print("Numero "f'ID {pokemon}')
   
    print(poke["id"])
    #for i in poke['stats']:
       # print(i['stat']['name'])

def main():
    global pokemon
    pokemon = str(input('Pokemon : '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    os.system('clear') # limpar linha pesquisa
    res=requests.get(api)
    poke=res.json()
    info_basica(poke)
    pegar_habilidades(poke)
    estatistica(poke)
    Id(poke)
    #print("ID.: ",poke["id"])
    #info_basica(poke)

#    if requests.status_code != 200:
#        print('Pokemon não encontrado')
#        exit()


if __name__ == '__main__':

    main()
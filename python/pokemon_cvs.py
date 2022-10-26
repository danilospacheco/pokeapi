import requests
import os
import csv
import pandas as pd
import argparse
#import pypokedex

filename = 'pokeapi.csv'

os.system('clear')



def main():
    #global pokemon
    #pokemon = str(input('Pokemon : '))
    api = 'https://pokeapi.co/api/v2/pokemon?limit=5&offset=0'
    os.system('clear') 
    res=requests.get(api)
    pokemons=res.json()
    #info_basica(poke)
    #pegar_habilidades(poke)
    #estatistica(poke)
    #Id(poke)

    
    with open('pokeapi.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['ID', 'Nome', 'Tipo', 'Habilidades', 'Estatistica']) # escreve strings no csv   
         
        for pokemon in pokemons['results']:
            requisicao = requests.get(pokemon['url']).json() # (pokemon['url'])
            spamwriter.writerow([requisicao["id"], requisicao["abilities"], requisicao["stats"]]) # escreve saida json
            

    #print("ID.: ",poke["id"])
    #info_basica(poke)

if __name__ == '__main__':

    main()
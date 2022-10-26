PokeAPI

Utilize o projeto em PYTHON para efetuar as consultas e para efetuar o provisionamento da infraestrutura o projeto TERRAFORM.


Procedimento:
Acesse o diretório python e execute o arquivo “pokemon_consulta.py” para efetuar a consulta do pokemon desejado, conforme exemplo abaixo:
# execução:
python3 pokemon_consulta.py

# Será solicitado o pokemon que deseja pesquisar, é possível passar o nome ou id.

Pokemon : 25

### CONSULTANDO INFORMAÇÕES ###
NOME DO POKEMON:
pikachu

NUMERO ID
25

pikachu É UM TIPO DE POKEMON:
electric

HABILIDADES DO  pikachu
static
lightning-rod

ESTATISTICA DO  pikachu
hp
attack
defense
special-attack
special-defense
speed

Após a consulta será apresentado os dados acima.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Acesse o diretório python e execute o arquivo “pokemon_cvs.py” desta forma o script criara um arquivo  “pokedex.csv” com a saída da api no formato json, conforme exemplo abaixo:
python3 pokemon_cvs.py

ID, Nome, Tipo, Habilidades, Estatistica
1,|[{'ability': {'name': 'overgrow', 'url': 'https://pokeapi.co/api/v2/ability/65/'}, 'is_hidden': False, 'slot': 1}, {'ability': {'name': 'chlorophyll', 'url': 'https://pokeapi.co/api/v2/ability/34/'}, 'is_hidden': True, 'slot': 3}]|,|[{'base_stat': 45, 'effort': 0, 'stat': {'name': 'hp', 'url': 'https://pokeapi.co/api/v2/stat/1/'}}, {'base_stat': 49, 'effort': 0, 'stat': {'name': 'attack', 'url': 'https://pokeapi.co/api/v2/stat/2/'}}, {'base_stat': 49, 'effort': 0, 'stat': {'name': 'defense', 'url': 'https://pokeapi.co/api/v2/stat/3/'}}, {'base_stat': 65, 'effort': 1, 'stat': {'name': 'special-attack', 'url': 'https://pokeapi.co/api/v2/stat/4/'}}, {'base_stat': 65, 'effort': 0, 'stat': {'name': 'special-defense', 'url': 'https://pokeapi.co/api/v2/stat/5/'}}, {'base_stat': 45, 'effort': 0, 'stat': {'name': 'speed', 'url': 'https://pokeapi.co/api/v2/stat/6/'}}]|

Após a consulta será gerado o arquivo pokedex.csv com os dados.


Observação.:
	Infelizmente não consegui criar os filtros necessário no arquivo .csv, mas assim que eu finalizar o script corretamente irei atualizar o documento e repositório.


Exemplos:
# o script vai solicitar o nome do pokemon para o user
python3 main.py
# passando o nome do pokemon como argumento
python3 main.py -pokemon=pikachu
# Forçando o script a obter os 10 pokemons
python3 main.py -poke10=true
Durante a execução sera pedido o nome de um pokemon como input. Caso o usuario não informe o nome de um pokemon o script buscara 10 pokemons na api pokeapi.co
Em seguida o script obtera o nome, habilidades e tipo do pokemon e fará a inserção ordenada por habilidade no arquivo Pokemon.csv
Exemplo Pokemon.csv:
Name,Ability,Type
charmander ,blaze  solar-power ,fire
charmeleon ,blaze  solar-power ,fire
charizard ,blaze  solar-power ,fire  flying
bulbasaur ,overgrow  chlorophyll ,grass  poison
ivysaur ,overgrow  chlorophyll ,grass  poison
venusaur ,overgrow  chlorophyll ,grass  poison
caterpie ,shield-dust  run-away ,bug
squirtle ,torrent  rain-dish ,water
wartortle ,torrent  rain-dish ,water
blastoise ,torrent  rain-dish ,water

#################################################################################################################################

Provisionamento da infraestrutura como código


Acesse o diretório terraform e execute o arquivo “main.tf” para provisionamento de toda infraestrutura, conforme exemplo abaixo:
#Inicializa o ambiente com o provider utilizado
Terraform init 
Mensagem no final: Terraform has been successfully initialized!

# Mostrar o plano de execução do terraform para provisionarmos a infra como código.
Terraform plan 

# Comando abaixo para criarmos.
Terraform apply  


# Deleta todos os recursos criados
Terraform destroy 


# recomendaçao de filmes biblioteca imdb

import requests
import json
import imdb #pip install imdbpy

def requisicao(titulo):
    try:
        #http://www.omdbapi.com/?i='+titulo+'&apikey=9cd86d79
        req = requests.get('https://www.omdbapi.com/?apikey=9cd86d79&t='+titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar(filme):
    print('')
    print('\tDETALHES DO FILME RECOMENTADO\t\n')
    print('Titulo: ',filme['Title'])
    print('Ano: ', filme['Year'])
    print('Gerero: ',filme['Genre'])
    print('Atores: ',filme['Actors'])
    print('Diretor: ',filme['Director'])
    print('Nota: ',filme['Ratings'][0]['Value'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não Encontrado!!')
        else:
            print('')
            print('\tDETALHES DO FILME DO USUARIO \t\n')
            print('Titulo: ',filme['Title'])
            print('Ano: ', filme['Year'])
            print('Gerero: ',filme['Genre'])
            print('Atores: ',filme['Actors'])
            print('Diretor: ',filme['Director'])
            print('Nota: ',filme['Ratings'][0]['Value'])
            print('')
            #printar 5 recomendações referentes ao genero e as 5 maiores notas
            
            ia =imdb.IMDb()
            top250 = ia.get_top250_movies()
            #search = ia.get_movie()

            cont=0
            print(f'\n\tRangink dos melhores filmes similares a {filme["Title"]}: \n')
            
            for i in range(0, 250):
                # First, retrieve the movie object using its ID
                movie = ia.get_movie(top250[i].movieID)

                genero = filme['Genre']
                film = genero.split(", ")
               
                if movie['genres'][0] or movie['genres'][1] == film[0]:
                    print('')
                    print(f"{cont+1}° Filme: {movie['title']}")
                    print(f"Genero: {movie['genres']}")
                    print(f"Nota: {movie['rating']}")
                    print('')
                    cont+=1
                    #printar(filme)
                if cont == 5:
                    print('Busca concluida. Volte sempre!\n')
                    exit()
            if cont == 0:
                print('Nada foi encontrado')
                exit()
                
            
            

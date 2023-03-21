#criando projeto de teste para data science
## 10 melhores filmes do cinema

import imdb #pip install imdbpy

#análise e manipulação de dados

ia =imdb.IMDb()
search = ia.get_top250_movies()

print('\n\tOs 10 melhores filmes do cinema: \n')
for i in range(10):
    print(f'{i+1}° - {search[i]}')


from filme import Filme
from serie import Serie
from play_list import Playlist
from collections.abc import MutableSequence


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
temp = Filme('Todo mundo em pânico', 2015, 100)
vingadores.dar_likes()
vingadores.dar_likes()
temp.dar_likes()
temp.dar_likes()
temp.dar_likes()
temp.dar_likes()
# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2017, 2)
demolidor = Serie('Demolidor', 2012, 3)
atlanta.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta, demolidor, temp]
play_list_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'tamanho do playlist {len(play_list_fim_de_semana)}')

for programacao in play_list_fim_de_semana:
    print(programacao)
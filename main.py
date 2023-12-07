import json


def informacoes_projeto():
    with open('dados/filtro.json', 'r', encoding='utf-8') as file:
        filtro_data = json.load(file)
        palavras_ofensivas = filtro_data['palavras_proibidas']

    nome_projeto = 'Projeto de Filtro de Palavras Ofensivas'

    total_palavras = len(palavras_ofensivas)

    objetivo = 'O objetivo principal deste projeto é oferecer um filtro de palavras ofensivas para identificar e filtrar conteúdo inadequado em textos.'

    print(f'Nome do projeto: {nome_projeto}')
    print(f'Total de palavras no filtro: {total_palavras}')
    print(f'Objetivo do projeto: {objetivo}')


if __name__ == '__main__':
    informacoes_projeto()

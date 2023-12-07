import json


def organizar_palavras_frases(arquivo_txt, arquivo_json):
    with open(arquivo_txt, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

        palavras = []
        frases = []

        for linha in linhas:
            # Verifica se a linha possui apenas uma palavra (sem espaços)
            if ' ' not in linha.strip():
                palavras.append(linha.strip())
            else:
                frases.append(linha.strip())

        data = {'palavras': palavras, 'frases': frases}

        with open(arquivo_json, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

        print(
            f"As palavras e frases do arquivo '{arquivo_txt}' foram organizadas e salvas em '{arquivo_json}'."
        )


organizar_palavras_frases('filtro.txt', 'organizado.json')

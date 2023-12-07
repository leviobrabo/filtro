def detectar_letras_duplicadas(arquivo_txt):
    palavras_com_duplicadas = []

    with open(arquivo_txt, 'r', encoding='utf-8') as file:
        for line in file:
            palavras = line.split()
            for palavra in palavras:
                palavra = palavra.lower()
                if len(set(palavra)) != len(palavra):
                    palavras_com_duplicadas.append(palavra)

    if palavras_com_duplicadas:
        print('Palavras com letras duplicadas encontradas:')
        print(palavras_com_duplicadas)
    else:
        print('Nenhuma palavra com letras duplicadas encontrada.')


# Exemplo de uso
detectar_letras_duplicadas('filtro.txt')

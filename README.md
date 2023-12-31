# Projeto de Filtro de Palavras Ofensivas

## Visão Geral

Este projeto consiste em um sistema de filtragem de palavras ofensivas em textos. Ele inclui diferentes ferramentas para detecção e organização de palavras, permitindo identificar palavras ofensivas com base em variações ortográficas, além de organizar e classificar palavras em diferentes contextos.

## Arquivos

-   `detecao_letras_duplicadas.py`: Um script Python para detectar palavras com letras duplicadas em um texto.
-   `filtro.json`: Um arquivo JSON contendo uma lista de palavras ofensivas.
-   `filtro.yaml`: Um arquivo YAML que pode ser usado para armazenar configurações relacionadas ao filtro de palavras ofensivas.
-   `organizador.py`: Um script Python para organizar palavras em categorias, como palavras e frases.

## Funcionamento

### Detecao_letras_duplicadas.py

Este script identifica palavras com letras duplicadas em um arquivo de texto. Ele examina cada linha do texto e, se encontrar uma palavra com letras repetidas, a adiciona a uma lista para identificação posterior.

**Como Usar:**

```bash
python detecao_letras_duplicadas.py arquivo.txt
```

Substitua `arquivo.txt` pelo nome do arquivo de texto que você deseja verificar.

### Filtro.json e Filtro.yaml

`filtro.json` e `filtro.yaml` são arquivos que contêm listas de palavras consideradas ofensivas. Você pode editar esses arquivos para adicionar, remover ou modificar palavras ofensivas de acordo com suas necessidades.

### Organizador.py

O script `organizador.py` categoriza palavras em listas separadas com base em suas características, como palavras individuais e frases.

**Como Usar:**

```bash
python organizador.py arquivo_entrada.txt arquivo_saida.json
```

Substitua `arquivo_entrada.txt` pelo nome do arquivo de entrada que contém palavras misturadas. O arquivo de saída será gerado em formato JSON (`arquivo_saida.json`).

### main.py


**Como Usar:**

```bash
python main.py
```
Lembre-se de acessar os arquivos em json/yaml/txt na pasta dados


## Objetivo

O objetivo principal deste projeto é oferecer ferramentas simples para identificar, classificar e organizar palavras ofensivas, facilitando a criação de filtros para conteúdo indesejado.

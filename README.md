# Análise Exploratória CNES.LT

Análise Exploratória dos dados de Leitos cadastrados no **Subsistema LT do CNES** para o **Estado de Goiás** com o objetivo de descrever a evolução da capacidade hospitalar durante a pandemia de Covid-19 em Goiás.

Para tal, extraimos o banco de dados diretamente do DataSUS por este [LINK](https://datasus.saude.gov.br/transferencia-de-arquivos/#) e transformamos os arquivos dbc's em csv por meio da biblioteca utilitária dbc2csv, disponível [neste repositório](https://github.com/greatjapa/dbc2csv).

Abaixo está o passo a passo de como reproduzir os resultados encontrados neste estudo.

### Pré-requisitos

1. Obrigatórios:
    - Python 3.8 ou Versão Superior

2. Recomendados:
    - GNU make
    
### Passo a Passo

1. Clone o repositorio
    
    Abra o terminal (se estiver usando Windows, utilize o git bash), navegue até o diretório desejado e clone o repositório,
    
    ```sh
    git clone https://github.com/willianfco/Atividade_DS_SES-GO.git
    ```

2. Crie um ambiente virutal e instale as bibliotecas utilizadas

    Crie um ambiente virtual de Python em sua máquina local para o projeto que estamos executando. Você pode utilziar a ferramenta que desejar para a criação deste ambiente. Ative o ambiente virtual e instale os requisitos usando `make`:
    
    ```sh
    make requirements
    ```

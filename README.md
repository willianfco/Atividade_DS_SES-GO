# Análise Exploratória CNES.LT

Repositório destinado à análise exploratória dos dados de leitos cadastrados no **Subsistema LT do CNES** para o **Estado de Goiás** com o objetivo de descrever a evolução da capacidade hospitalar durante a pandemia de Covid-19 em Goiás.

Para tal, extraí os bancos de dados do CNES.LT de janeiro de 2019 à novembro de 2022 diretamente do DataSUS por este [LINK](https://datasus.saude.gov.br/transferencia-de-arquivos/#) e transformei os arquivos dbc's em csv por meio da biblioteca utilitária dbc2csv, disponível [neste repositório](https://github.com/greatjapa/dbc2csv).

As análises nos notebooks nomeados `AED` e `AED_Plotly` são as mesmas, contudo em `AED_Plotly` foi utilizada a biblioteca Plotly Express, que cria gráficos dinâmicos em HTML/JavaScript que não são renderizados pelo visualizador estático do GitHub. Para visualização dos gráficos interativos, recomenda-se acesso em:  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KmWxYn1hmskDewwK3AGW2txd5Ch2wvPx?usp=sharing)

A fim de apresentar outras visualizações interativas com uso de mapas, também foram desenvolvidos dois paineis utilizando o Tableau Public:

[1. Análises - Leitos Exclusivos Covid-19](https://public.tableau.com/views/Anlisegeogrfica-LeitosCovid-19/PaineldeAnlise?:language=pt-BR&publish=yes&:display_count=n&:origin=viz_share_link)

- Onde foram analisadas as evoluções temporais e espaciais do número de leitos classificados como:
    - UTI SRAG Covid-19 - Adulto
    - UTI SRAG Covid-19 - Pediátrico
    - Suporte Ventilatório Pulmonar - Covid-19

[2. Análises - Leitos UTI Geral](https://public.tableau.com/views/Anlisegeogrfica-LeitosUTIGeral/PaineldeAnlise?:language=pt-BR&publish=yes&:display_count=n&:origin=viz_share_link)

- Onde foram analisadas as evoluções temporais e espaciais do número de leitos classificados como:
    - UTI ADULTO - TIPO I
    - UTI ADULTO - TIPO II
    - UTI ADULTO - TIPO III
    - UTI PEDIATRICA - TIPO I
    - UTI PEDIATRICA - TIPO II
    - UTI NEONATAL - TIPO I
    - UTI NEONATAL - TIPO II
    - UTI NEONATAL - TIPO III
    - UTI DE QUEIMADOS
    - UTI CORONARIANA - TIPO II
    - UTI CORONARIANA - TIPO III

Destacamos alguns pontos interessantes que podem ser observados pelas análises gráficas acerca da evolução dos leitos exclusivos para covid-19 e dos leitos de UTI Geral no estado de Goiás.

<div style="background-color:white; height: 100%">
<h1 align="center"> <img width=1200px src=img/leitos_cov19.png> </h1>
</div>

<div style="background-color:white; height: 100%">
<h1 align="center"> <img width=1200px src=img/leitos_cov19_sus.png> </h1>
</div>

<div style="background-color:white; height: 100%">
<h1 align="center"> <img width=1200px src=img/leitos_uti.png> </h1>
</div>

Com base nos gráficos acima, podemos identificar que:

- Há uma redução considerável no número de leitos exclusivos para Covid-19 disponibilizados para o SUS no período que antecede o pico de letalidade do Covid-19 no Brasil (abril de 2021), variando de 413 para 238 leitos no período de novembro de 2020 à fevereiro de 2021.

- Há um aumento robusto do número de leitos totais e disponibilizados para o SUS após o pico histórico de contaminações no Brasil (Fevereiro de 2021), demonstrando uma estratégia responsiva da SES visando a sustentabilidade do sistema de saúde neste período de estresse da rede de atenção. No caso dos leitos disponibilizados para o SUS, o número de leitos de UTI foi de 238 para 801 no intervalo de 1 mês (fevereiro->março/2021) e continuou crescendo até outubro do mesmo ano, atingindo um pico de 1006 leitos disponíveis. Esta alteração se dá tanto pelo aquisição de novos leitos, quanto pelo aumento da disponibilização dos leitos já existentes, que permanesceu alta até 2022.

- Com o avanço da vacinação/reforço imunológico e a redução da letalidade potencial das novas variantes do SARS-CoV-2, já no ano de 2022, podemos observar um movimento de transformação dos Leitos Exclusivos para Covid-19 em Leitos de UTI Geral, principalmente Leitos de UTI Adulto - Tipo II. Esta movimentação é importante, pois amplia a capacidade da atenção terciária para diversos agravos, passando de 1434 leitos de UTI Adulto, Pediátrica, Neonatal, Queimados e Coronáriana para 2107 durante todo o período analisado.

Já na análise espacial, podemos verificar o seguinte comportamento:

Leitos UTI - Janeiro de 2019             |  Leitos UTI - Novembro de 2022 
:-------------------------:|:-------------------------:
![](https://github.com/willianfco/Atividade_DS_SES-GO/blob/master/img/mapa_leitos_jan19.png)  |  ![](https://github.com/willianfco/Atividade_DS_SES-GO/blob/master/img/mapa_leitos_nov22.png)

- Ainda relacionado à transformação dos Leitos Covid-19 em Leitos de UTI Geral, é possivel observar que esta ação expandiu o número de leitos para outras regiões do estado, o que possivelmente trará benefícios para o sistema de saúde, visto que realiza uma aproximação do serviço aos cidadãos das regiões que não tinham leitos próximos e precisavam ser deslocados para a região central/metropolitana para terem acesso aos leitos em unidades de tratamento intensivo.

Com base nas análises acima, podemos concluir que a SES-GO executou uma estratégia de expansão eficiente dos leitos em períodos críticos do Covid-19 e, após o arrefecimento da pandemia, manteve os novos leitos da atenção terciária, trazendo impactos positivos diversificados na saúde pública, tanto no ponto de vista da manutenção dos investimentos executados no período anterior, quanto na regionalização do acesso.

## Execução em Máquina Local

Abaixo está o passo a passo de como trabalhar com os códigos deste estudo.

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

2. Crie um ambiente virtual e instale as bibliotecas utilizadas

    Crie um ambiente virtual de Python em sua máquina local para o projeto que estamos executando. Você pode utilziar a ferramenta que desejar para a criação deste ambiente. Ative o ambiente virtual e instale os requisitos disponibilizados em `requirements.txt` usando `make`:
    
    ```sh
    make requirements
    ```

## Licença

O projeto está disponibilizado sob a licença Creative Commons Zero v1.0 Universal, que renuncia ao interesse de direitos autorais em uma obra e a dedica ao domínio público mundial, sob esta licença está permitido o uso comercial e privado; modificação e distribuição dos códigos aqui disponibilizados. Para mais informações, verificar em `LICENSE`.

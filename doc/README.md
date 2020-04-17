# Executar projeto sem o docker

<h2>Instalar e iniciar</h2>

1 - Python3 instalado no dispositovo<br>
2 - Clonar o repositório:
```
$ gi clone https://github.com/lbetol/crawler_semantix.git

```
3 - Instalar via pip:
```
$ pip install Scrapy
# pip install scrapy-fake-useragent
$ pip install ipdb

```
4 - Dentro do repositório clonado na pasta db digitar o comando:<br>
```
$ scrapy crawl nasdaq
$ scrapy crawl ibovespa
$ scrapy crawl usdbrl
```
5 - Estes comandos iram criar um arquivo sqlite com o nome semantixdb.db. <br>

# Detalhes do projeto

Cada crawler foi feito para ser utilizado de forma independente.
Ao executar o docker, automaticamente executará o arquivo iniciar.py.
O arquivo iniciar.py executa os 3 crawler automaticamente.


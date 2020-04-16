# Projeto web crawler
# Processo seletivo para a empresa Semantix
# ------------------------------------------
# Autor: Alberto Barrios
# Data: 11/04/2020
# ------------------------------------------

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

# classe SemantixPipeline é responsável por toda a interação
# da aplicação com o banco de dados. Desde a criação do banco
# a inserção de dados no banco de dados.
class SemantixPipeline(object):

    # __init__ irá conectar no banco de dados
    # Se não tiver banco para ser conectado ele irá criar o banco
    def __init__(self):
        self.criar_conexao()
        self.criar_tabela_nasdaq()
        self.criar_tabela_ibovespa()
        self.criar_tabela_usdbrl()
        self.criar_tabela_brl()

    # criar_conexao irá fazer a conexão entre a aplicação ao banco de dados sqlite
    def criar_conexao(self):
        self.conecta = sqlite3.connect("semantixdb.db")
        self.banco = self.conecta.cursor()

    def fecha_banco(self):
        self.banco.close()

    def __del__(self):
        self.fecha_banco()

    # criar_tabela cria todas as tabelas que serão utilizadas na aplicação
    def criar_tabela_nasdaq(self):
        self.banco.execute(""" create table if not exists nasdaq(
                            name text,
                            last_usd text,
                            high_usd text,
                            low_usd text,
                            chg text,
                            chper text,
                            vol text,
                            timenq str)""")

    def criar_tabela_ibovespa(self):
        self.banco.execute(""" create table if not exists ibovespa(
                            name text,
                            last_rs text,
                            high_rs text,
                            low_rs text,
                            chg text,
                            chgper text,
                            vol text,
                            time varchar(8)
                            )""")

    def criar_tabela_usdbrl(self):
        self.banco.execute(""" create table if not exists usdbrl(
                            currency text,
                            value text,
                            change text,
                            perc text,
                            timestamp text
                            )""")

    def criar_tabela_brl(self):
        self.banco.execute(""" create table if not exists brl(
                            name text primary key,
                            last_usd text null,
                            high_usd text null,
                            low_usd text null,
                            last_rs text,
                            high_rs text,
                            low_rs text,
                            chg text,
                            chg_per text,
                            vol text,
                            time varchar(8),
                            timestamp
                            )""")

    # Função process_item prepara todos os itens
    # para serem enviados as suas respectivas tabelas
    def process_item(self, item, spider):
        self.insere_cotacao(item)
        return item

    # insere_cotacao insere os itens na tabela usbrl
    def insere_cotacao(self, item):
        self.banco.execute("""insert into usdbrl (currency,value,change,perc,timestamp) values (?,?,?,?,?)""", (
            str(item['currency'][0]),
            str(item['value'][0]),
            str(item['change'][0]),
            str(item['perc'][0]),
            str(item['timestamp'][0])
        ))
        self.conecta.commit()

    # insere_nasdaq insere os itens na tabela nasdaq
    def insere_nasdaq(self, item):
        for x in range(0, 103):
            self.banco.execute("""insert into nasdaq (name,last_usd,high_usd,low_usd,chg,chper,vol,timenq) values (?,?,?,?,?,?,?,?)""", (
                str(item['name'][x]),
                str(item['last_usd'][x]),
                str(item['high_usd'][x]),
                str(item['low_usd'][x]),
                str(item['chg'][x]),
                str(item['chper'][x]),
                str(item['vol'][x]),
                str(item['timenq'][x])
            ))
            self.conecta.commit()

    # insere_ibovespa insere os itens na tabela ibovespa
    def insere_ibovespa(self, item):
        for x in range(0, 73):
            self.banco.execute("""insert into ibovespa values (?,?,?,?,?,?,?,?)""", (
                str(item['name'][x]),
                str(item['last_rs'][x]),
                str(item['high_rs'][x]),
                str(item['low_rs'][x]),
                str(item['chg'][x]),
                str(item['chper'][x]),
                str(item['vol'][x]),
                str(item['time'][x])
            ))
            self.conecta.commit()

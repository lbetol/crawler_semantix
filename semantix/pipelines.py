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

class SemantixPipeline(object):

    # __init__ irá conectar no banco de dados
    # Se não tiver banco para ser conectado ele irá criar o banco
    def __init__(self):
        self.criar_conexao()
        self.criar_tabela()

    # criar_conexao irá fazer a conexão entre a aplicação ao banco de dados sqlite
    def criar_conexao(self):
        self.conecta = sqlite3.connect("semantixdb.db")
        self.banco = self.conecta.cursor()

    # criar_tabela cria todas as tabelas que serão utilizadas na aplicação
    def criar_tabela(self):
        self.banco.execute(""" create table if not exists nasdaq(
                            name text,
                            last_usd text,
                            high_usd text,
                            low_usd text,
                            chg text,
                            chper text,
                            vol text,
                            time text
                            )""")
        self.banco.execute(""" create table if not exists ibovespa(
                            name text,
                            last_rs text,
                            high_rs text,
                            low_rs text,
                            chg text,
                            chgper text,
                            vol text,
                            time text
                            )""")

        self.banco.execute(""" create table if not exists usdbrl(
                            currency text,
                            value text,
                            change text,
                            perc text,
                            timestamp text
                            )""")


    def process_item1(self, item, IbovespaSpider):
        self.insere_ibovespa(item)
        return item

    def process_item2(self, item, UsdBrlSpider):
        self.insere_cotacao(item)
        return item

    def process_item(self, item, NasdaqSpider):
        self.insere_nasdaq(item)
        return item

    def insere_cotacao(self, item):
        self.banco.execute("""insert into usdbrl values (?,?,?,?,?)""", (
            item['currency'],
            item['value'],
            item['change'],
            item['perc'],
            item['timestamp']
        ))
        self.conecta.commit()

    def insere_nasdaq(self, item):
        self.banco.execute("""insert into nasdaq values (?,?,?,?,?,?,?,?)""", (
            item['name'][0],
            item['last_usd'][0],
            item['high_usd'][0],
            item['low_usd'][0],
            item['chg'][0],
            item['chper'][0],
            item['vol'][0],
            item['time'][0]
        ))
        self.conecta.commit()

    def insere_ibovespa(self, item):
        self.banco.execute("""insert into ibovespa values (?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['last_rs'],
            item['high_rs'],
            item['low_rs'],
            item['chg'],
            item['chper'],
            item['vol'],
            item['time']
        ))
        self.conecta.commit()

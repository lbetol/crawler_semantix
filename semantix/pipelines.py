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
        self.criar_tabela()

    # criar_conexao irá fazer a conexão entre a aplicação ao banco de dados sqlite
    def criar_conexao(self):
        self.conecta = sqlite3.connect("semantixdb.db")
        self.banco = self.conecta.cursor()

    # criar_tabela cria todas as tabelas que serão utilizadas na aplicação
    def criar_tabela(self):
        self.banco.execute(""" create table if not exists nasdaq(
                            name text,
                            last_usd text null,
                            high_usd text null,
                            low_usd text null,
                            chg text null,
                            chper text null,
                            vol text null,
                            timenq varchar(8) null
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

        self.banco.execute(""" create table if not exists brl(
                            name text,
                            last_usd text null,
                            high_usd text null,
                            low_usd text null,
                            last_rs text,
                            high_rs text,
                            low_rs text,
                            chg text,
                            chg_per text,
                            vol text,
                            time text,
                            timestamp
                            )""")

    # Função process_item prepara todos os itens
    # para serem enviados as suas respectivas tabelas
    def process_item(self, item, spider):
        if spider == "ibovespa":
            self.insere_ibovespa(item)
        if spider == "nasdaq":
            self.insere_nasdaq(item)
        if spider == "usdbrl":
            self.insere_cotacao(item)
        return item

    # insere_cotacao insere os itens na tabela usbrl
    def insere_cotacao(self, item):
        self.banco.execute("""insert into usdbrl values (?,?,?,?,?)""", (
            item['currency'][0],
            item['value'][0],
            item['change'][0],
            item['perc'][0],
            item['timestamp'][0]
        ))
        self.conecta.commit()

    # insere_nasdaq insere os itens na tabela nasdaq
    def insere_nasdaq(self, item):
        self.banco.execute("""insert into nasdaq values (?,?,?,?,?,?,?,?)""", (
            item['name'][0],
            item['last_usd'][0],
            item['high_usd'][0],
            item['low_usd'][0],
            item['chg'][0],
            item['chper'][0],
            item['vol'][0],
            item['timenq'][0]
        ))
        self.conecta.commit()

    # insere_ibovespa insere os itens na tabela ibovespa
    def insere_ibovespa(self, item):
        self.banco.execute("""insert into ibovespa values (?,?,?,?,?,?,?,?)""", (
            item['name'][0],
            item['last_rs'][0],
            item['high_rs'][0],
            item['low_rs'][0],
            item['chg'][0],
            item['chper'][0],
            item['vol'][0],
            item['time'][0]
        ))
        self.conecta.commit()

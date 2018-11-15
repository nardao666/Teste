import sqlite3
import collections
import csv

# passei o arquivo csv para o sqlite3
# Arquivo do bando de dados
# https://drive.google.com/open?id=1Mj771B4-okhEEHvKaELm33KFs58-jmA0

conn = sqlite3.connect('kickstarter.db') #comando para conectar com o BD
cursor = conn.cursor() # ponteiro para executar as funções do sqlite

# Declaração da variaveis utilizadas
l = [] 
list_country =[]
cnt = []

# Comando para fazer a seleção no BD
cursor.execute("""
SELECT country FROM project;
""")

# Passa todos os valores do BD para a lista l
for linha in cursor.fetchall():
	l.append(linha)

# Passa todos os pais para a list_country sem repetir
for i in l:
	if i not in list_country:
		list_country.append(i)

# Conta qtas vezes o pais apareceu na lista l e coloca a lista cnt
for i in range(0,len(list_country)):
	a=list_country[i]
	cnt.append(l.count(a))

# Escreve em um arquivo csv
with open("saida_1_1_1.csv", "w", newline='') as csvfile:
	c =csv.writer(csvfile, delimiter=',', quoting = csv.QUOTE_MINIMAL)
	c.writerow(["Pais","qtd_projetos"])
	for i in range(0,len(list_country)):
		c.writerow([list_country[i],cnt[i]])

# Fecha a conexão com BD
conn.close()

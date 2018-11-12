import sqlite3

# passei o arquivo csv para o sqlite3
# Arquivo do bando de dados
# https://drive.google.com/open?id=1Mj771B4-okhEEHvKaELm33KFs58-jmA0

conn = sqlite3.connect('kickstarter.db') #comando para conectar com o BD
cursor = conn.cursor() # ponteiro para executar as funções do sqlite

# Declaração da variaveis utilizadas
l = []
lista =[]
count = 0

conn = sqlite3.connect('kickstarter.db') #comando para conectar com o BD
cursor = conn.cursor() # ponteiro para executar as funções do sqlite

# Comando para fazer a seleção no BD
cursor.execute("""
SELECT category, pledged, usd_pledged FROM project WHERE country="US" AND state="successful"
""")

# Passa todos os valores do BD para a lista l
for linha in cursor.fetchall():
	l.append(linha)

# Conta os valores que passaram da arrecadação
for i in range(0,len(l)):
	count = count + (l[i][1] - l[i][2])

# Fecha a conexão com BD
conn.close()



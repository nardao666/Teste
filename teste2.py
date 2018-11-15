import sqlite3
import collections
import heapq

# passei o arquivo csv para o sqlite3
# Arquivo do bando de dados
# https://drive.google.com/open?id=1Mj771B4-okhEEHvKaELm33KFs58-jmA0

conn = sqlite3.connect('kickstarter.db') #comando para conectar com o BD
cursor = conn.cursor() # ponteiro para executar as funções do sqlite

# Declaração da variaveis utilizadas
l = []
lista =[]
cnt = []
category =[]
usdpled = []
index_maior = []
list_cat = []
list_pled = []

# Comando para fazer a seleção no BD
cursor.execute("""
SELECT category, usd_pledged FROM project WHERE state="successful";
""")

# Passa todos os valores do BD para a lista l
for linha in cursor.fetchall():
	l.append(linha)

# Passa todos os pais para a list_country sem repetir
for i in range(0,len(l)):
	a=l[i][0]
	if a not in lista:
		lista.append(a)

# Separando a lista e duas lista category e usdpled		
for i in range(0,len(l)):
	a=l[i][0]
	b=l[i][1]
	category.append(a)
	usdpled.append(b)

# Conta qtas vezes o pais apareceu na lista l e coloca a lista cnt
for i in range(0,len(lista)):
	a=lista[i]
	cnt.append(category.count(a))

maior = heapq.nlargest(3,cnt) #mostra os 3 maiores da lista cnt

# Posição dos 3 maiores
for i in maior:
	index_maior.append(cnt.index(i))

# A list_cat mostra quem são os 3 maiores
for i in index_maior:
	a= category[i]
	list_cat.append(a)

# Pega o soma os valores arrecados em cada category
for i in range(0,len(list_cat)):
	a = list_cat[i]
	count_usd = 0
	for j in range(0,len(l)):
		if l[j][0] == a :
			count_usd = count_usd + l[j][1]
	list_pled.append(count_usd)
	
# Imprimindo a resposta
for i in range(0,len(list_cat)):
	print (	list_cat[i], list_pled[i])

# Fecha a conexão com BD
conn.close()

# Resposta em ordem cresencete
#
#	Photography 13776535.278375827
#	Webseries 17754841.20121909
#	Indie Rock 18869296.158468843


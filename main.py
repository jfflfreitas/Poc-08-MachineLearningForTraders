from coinmarketcap import Market
import matplotlib.pyplot as plt
import pandas as pd
import time
# #---------------------------------------------------------------------------------------#

#Aula 01
# #instancia a função market
# market = Market()

# #inserindo os valores dentro de ticker
# ticker = market.ticker(convert = "BRL")

# #convertendo a moeda de USD para BRL
# # converted_exchange = market.ticker(start= 0, limit= 1, convert= "BRL")

# #extrai 'data' de ticker
# data = ticker['data']

# #identifica o preço do bitcoin
# btc =data['1']
# print(btc)
# #---------------------------------------------------------------------------------------#

# #---------------------------------------------------------------------------------------#
#Aula 02
# a = [1, 2, 3, 4, 5]
# b = [11, 23, 42, 17, 25]
# fig = plt.figure(figsize=(10,10))
# ax = fig.gca()
# ax.plot(a,b, label = "teste")
# plt.legend()
# plt.show()
# #---------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------#
#Aula 03
# nome = "john"
# salario = "50000"
# print(nome, salario)

# grava = open("john.csv", "a")
# grava.write(str(nome+'\n'))
# grava.write(str(salario))
# grava.close()
# df = pd.read_csv("john.csv")
# print(df)

def recebe_btc(lista_btc):
    market = Market()
    ticker = market.ticker(convert = "BRL")
    data = ticker['data']['1']['quotes']['BRL']['price']
    btc = data
    lista_btc.append(btc)
    return lista_btc

def recebe_xrp(lista_xrp):
    market = Market()
    ticker = market.ticker(convert = "BRL")
    data = ticker['data']['52']['quotes']['BRL']['price']
    xrp = data
    lista_xrp.append(xrp)
    return lista_xrp

lista_btc = []
lista_xrp = []
fig = plt.figure(figsize=(10,10))
fig2 = plt.figure(figsize=(10,10))
ax = fig.gca()
ax2 = fig2.gca()

while True:
    ax.clear()
    ax2.clear()
    ax.plot(recebe_btc(lista_btc))
    ax2.plot(recebe_xrp(lista_xrp))
    plt.pause(1)


#---------------------------------------------------------------------------------------#
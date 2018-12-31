from coinmarketcap import Market

#instancia a função market
market = Market()

#inserindo os valores dentro de ticker
ticker = market.ticker()

#convertendo a moeda de USD para BRL
converted_exchange = market.ticker(start= 0, limit= 1, convert= "BRL")

#extrai 'data' de ticker
data = converted_exchange['data']

#identifica o preço do bitcoin
btc_price =data['1']['quotes']['BRL']['price']
print(btc_price)
import json
import requests

#Criando as variaveis que serao utlizadas no programa
data_output = {}
image_list = []

#Abrindo o arquivo de saida dump.json
file = open("dump.json", "w")

#Lendo o arquivo de entrada input-dump
with open('input-dump', 'r') as f:
	#Ordenando a entrada e armazenado esse dados em uma lista
	data = sorted(f.readlines())
	#Pegando o primeiro productid 
	productId = json.loads(data[0])['productId']

#Percorrendo a lista que foi realizada a leitura acima
for i in data:	
	#Transformando a o i que esta como string em dicionario
	i = json.loads(i)
	#Verificando se a lista tem tamanho > 2 e se o productid eh o mesmo
	if len(image_list) > 2 and i['productId'] == productId:
		continue	

	#Verificando se o productid eh o mesmo e se a lista eh menor que 3
	if i['productId'] == productId and len(image_list) < 3:
		#Verificando se a requisicao que foi realizada tem o status 200(ok), caso positivo eh adicionado na lista de imagens
		if requests.get(i['image']).status_code == 200 :
			image_list.append(i['image'])
	else:
		#Gravando uma linha no dump de saida com as url coletadas(no max 3) e com o productid
		json.dump({'productId': productId, 'images': image_list}, file,sort_keys=False)
		file.write('\n')
		productId = i['productId']
		image_list = []
#Realizando fechamento do arquivo
file.close()
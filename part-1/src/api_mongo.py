from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask_pymongo import PyMongo
import datetime
import dateutil.relativedelta
import ast
import json
import hashlib

app = Flask(__name__)

#Configurando o nome do db
app.config['MONGO_DBNAME'] = 'log_events'
#Configurando a string de conexao ao mongodb
app.config['MONGO_URI'] = 'mongodb://localhost/log_events'

#Realizando a conexao com o mongodb
mongo = PyMongo(app)

@app.route('/v1/products', methods=['POST'])
def verify_request():
	'''
	Funcao para realizar a checagem se uma request foi feita com o mesmo corpo em ate 10 minutos,
	caso a request tinha sido feito em < 10 eh retornado um erro 403 Forbidden, caso contrario
	eh retornado um 200 Ok e o registor eh inserido no mongdob como um registro TLL que ira expirar em 10m
	Input: Json ou uma lista de json
	- {'id': '123', 'name': 'teste123'}
	Output:
	Caso de sucesso:
	- 200 OK
	Caso de forbidden:
	- 403 Forbidden
	'''
	#Especificando a collection no mongodb e criando um index para exclusao do registro a cada 10minutos
	db = mongo.db.logs_events
	db.create_index("data_mongodb_db", expireAfterSeconds= 10*60)
	#Pegando a data atual do sistema
	data_atual = datetime.datetime.utcnow()
	#Percorrendo os dados de entrada
	for dados in json.loads(request.get_data()):
	   #Criando um md5 com o valor do request para garantir que nao tenha request duplicado
	   new_dados = {"md5" : hashlib.md5(json.dumps(dados)).hexdigest()}
	   #Verificando se existe o mesmo md5 no banco, caso positivo retornar 403 Forbidden caso negativo retornar 200 OK
	   if db.find_one(new_dados):
	      return Response('403 Forbidden',status=403)

	   new_dados["data_mongodb_db"] = data_atual
	   db.insert(new_dados)
	   return Response('200 OK',status=200)


#Inicando a api web
if __name__ == '__main__':
    app.run(host='0.0.0.0')

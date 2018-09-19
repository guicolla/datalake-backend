### First API
The first API is to deny requests that have the same body within a 10 minute interval.

If you have a kubernetes cluster you can deploy the application, the services and auto scaling with yaml in kubernetes folder but if you just want to test the application you can test with docker-compose following the next steps:
#### 1º First you need to start the docker-compose with the following command:
```docker-compose up```
#### 2º You need to enter in the container for test the API
```docker exec -it api bash```
#### 3º You need to call the api for test the result
```curl -XPOST http://localhost:5000/v1/products -d '[{"id": "123", "name": "teste"}]'```
#### 4º Call again the API for test the 403 Forbidden error
```curl -XPOST http://localhost:5000/v1/products -d '[{"id": "123", "name": "teste"}]'```

### Running the test
The folder test have the scripts for test the API
#### Prerequisites
* Mongodb
* pymongo
* flask_pymongo
* flask
* python-dateutil

#### Running
First you need to start the API with the following command:
```python app.py```

After you just need to run the test:
```python test.py```

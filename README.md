# Datalake Backend
This project have 2 APIs, one for validate a request and one for validate the status of URLs

## Prerequisites 
* Docker version 18.06.1
* docker-compose version 1.22.0

## Installing Docker and Docker Compose
For install the docker you can follow the steps in link below:
```https://docs.docker.com/install/linux/docker-ce/ubuntu/```
For install the docker-compose you can follow the steps in link below:
```https://docs.docker.com/compose/install/#install-compose```


## Running the APIs

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

### Second API
The second API is to eliminate URLs that can return status 404 and generate a list with no more than 3 URLs per id with status 200

To test the URL API you need to run a docker container and follow the next steps:
#### 1º First you need to create a docker container:
```docker run --name api_url -dit colla/api_url```
#### 2º Second you need to enter in container:
```docker exec -it api_url bash```
#### 3º You need to execute the URL API
```cd && python api_url.py```
#### 4º Visualize the results in dump.json
```head dump.json```

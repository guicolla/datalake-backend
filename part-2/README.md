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

### Running the test
Inside the folder test have a scripts for test the API
#### Prerequisites
* Python
* Ruby

#### First you need to run the ruby API
```url-aggregator-api.rb```
#### After you just need to run the API
```python app.py```

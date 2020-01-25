## SaleskenProblemSolving
- Clone github and change dir to "SaleskenProblem"
`git clone `
- Create virtual environment  `virtualenv --python=python3.6 venv`
- Activate virtual environment `source venv/bin/activate`
- Install requirements.txt `pip install -r requirements.txt`

### Problem 1 - 
Run problem_statement_1.py in python shell. It will create .csv of result with misspelt_name and list of ids for each misspelt city name.

### Problem 2 -
Run rest_api.py in Terminal `python rest_api.py` to start REST Api of get similar sentences.

- Test REST Api by python - 
```
import requests 
import json 
import ast 
corpus = ["Football is played in Brazil" ,"Traveling is good for health","Cricket is played in India","People love traveling in winter"]
headers = {'Content-Type':'application/json'} 
temp = requests.post(url='http://0.0.0.0:8000/get-similar-sent' ,data=json.dumps({'list_of_sentences':corpus}), headers=headers,verify=True) 
result = ast.literal_eval(temp.text) 
print(result)
```
- Test REST Api by curl - 
```
curl -d '{"list_of_sentences":["Football is played in Brazil" ,"Traveling is good for health","Cricket is played in India","People love traveling in winter"]}' -H 'Content-Type: application/json' -X POST http://0.0.0.0:8000/get-similar-sent
```

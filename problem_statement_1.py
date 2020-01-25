import pandas as pd 
from tqdm import tqdm
correct_cities = pd.read_csv("Correct_cities.csv")
misspelt_cities = pd.read_csv("Misspelt_cities.csv")

def frequency_true(var):
    count = 0
    for i in var:
        if i == True:
            count=count+1
    return count

result = {}

for i in tqdm(range(len(misspelt_cities))):
    misspelt_name = misspelt_cities.loc[i]['misspelt_name']
    country = misspelt_cities.loc[i]['country']
    correct_cities_country = correct_cities[correct_cities['country'] == country]
    id = []
    freq = 0

    for name in correct_cities_country['name']:
        if len(misspelt_name) == len(name):
            temp = [x==y for x,y in zip([char for char in name.lower()],[char for char in misspelt_name.lower()])]
            temp2 = frequency_true(temp)
            if freq == temp2:
                id.append(list(correct_cities_country[correct_cities_country['name']==name]['id'])[0])
            if freq < temp2:
                freq = temp2
                id = [list(correct_cities_country[correct_cities_country['name']==name]['id'])[0]]

    result[misspelt_name] = id
    
result1 = result
result = pd.DataFrame(result.items(),columns = ['misspelt_name','ids'])

result.to_csv('result.csv')
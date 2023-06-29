# make a get request to fetch 10 t or f questions
# parse the JSON response and replace the value of question_data
import requests

parameters = {
    'amount':10,
    'type': 'boolean'
}
response = requests.get(url='https://opentdb.com/api.php', params= parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']


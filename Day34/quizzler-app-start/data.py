import requests


def load_question_data():
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    data = response.json()
    return data['results']

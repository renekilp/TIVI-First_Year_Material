import requests


def random_cn_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']
        print(joke)


random_cn_joke()

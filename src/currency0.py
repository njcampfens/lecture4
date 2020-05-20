import requests

def main():
    ACCESS_KEY = '9b4bcbf2f24dec7c28e08c300da9236d'
    base = 'USD'
    symbols = 'EUR'
    url = f'http://data.fixer.io/api/latest?access_key={ACCESS_KEY}base={base}symbols={symbols}'


    res = requests.get(url)
    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    data = res.json()
    print(data)

if __name__ == '__main__':
    main()

import requests

def main():

    ACCESS_KEY = '9b4bcbf2f24dec7c28e08c300da9236d'
    url = f'http://data.fixer.io/api/latest?access_key={ACCESS_KEY}'

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception('ERROR: API request unsuccessful')

    data = res.json()

    rate = data['rates']['USD']

    print(f'1 EUR is equal to {rate} USD)')

if __name__ == '__main__':
    main()

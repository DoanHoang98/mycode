import requests

requests.get(url='https://github.com/requests/requests/issues/3863', proxies={'https': 'socks5://127.0.0.1:9150'})
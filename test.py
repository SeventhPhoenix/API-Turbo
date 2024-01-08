import requests

url = 'https://example.url.com'

data = requests.get(url)

print(data.content)
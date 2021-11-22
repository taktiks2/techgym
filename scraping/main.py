import requests

url: str = 'https://techgym.jp/?cat=2'
response: str = requests.get(url)
response.encoding = response.apparent_encoding

print(response.text)
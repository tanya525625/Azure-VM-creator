from http import cookies
import requests
import responses

url = 'http://127.0.0.1:5000/'
cookies = dict(name='jerry', password='888')

response = requests.get(url, headers={'set-cookie': 'mk=lkmj'})
response = requests.get(url, cookies=cookies)
print(response.text)
custom_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}


response = requests.get(url)

print(response.headers)


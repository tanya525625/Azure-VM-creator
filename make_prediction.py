import os
import http.cookies
import requests
import responses

# cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
# # name = cookie.get("name")
# # if name is None:
# #     print("Cookies!!!")
# # else:
# #     print("Content-type: text/html\n")
# #     print("Cookies:")
# #     print(name.value)
#
#
url = 'http://127.0.0.1:5000'
r = requests.get(url)
# print(cookie)
print(r.cookies)
# session = requests.Session()
# with responses.RequestsMock() as rsps:
#     r = session.get('http://127.0.0.1:5000')

print(r.text)
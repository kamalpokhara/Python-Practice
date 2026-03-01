import requests

r = requests.get("http://facebook.com")

print(r.text)

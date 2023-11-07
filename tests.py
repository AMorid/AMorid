import requests
url = "https://api.github.com/users/moridaziz)"
pakketje = requests.get(url)
print(pakketje.json())

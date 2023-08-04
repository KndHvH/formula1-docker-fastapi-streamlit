



import requests


response = requests.get(f"http://localhost:8000/drivers")
data = response.json()
print(type(response))

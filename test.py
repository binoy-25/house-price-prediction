import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "features": [3, 2, 1500, 1, 2005]
}

response = requests.post(url, json=data)

print(response.json())
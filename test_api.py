import requests

house = {"size": 150, "nb_rooms": 3, "garden": 1}

response = requests.post("http://localhost:8000/predict", json=house)
print(response.status_code)
print(response.json())

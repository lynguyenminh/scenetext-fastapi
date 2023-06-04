import requests

url = "http://0.0.0.0:4002/api/detection/craft/"
filename = "test-case.jpg"

with open(filename, "rb") as f:
    response = requests.post(url, files={"file": f}, data={"threshold": 0.5})

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)

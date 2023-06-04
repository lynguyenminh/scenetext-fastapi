import requests

url = "http://localhost:4001/api/detection/yolov8/"
filename = "test-case.jpg"

with open(filename, "rb") as f:
    response = requests.post(url, files={"file": f}, data={"threshold": 0.5})

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)

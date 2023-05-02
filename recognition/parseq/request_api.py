import requests

url = 'http://0.0.0.0:4003/api/recognition/parseq/'
files = {'file': open('test-case.jpg', 'rb')}
coordinates = [107, 11, 142, 31]
data = {'coordinates': coordinates}

response = requests.post(url, files=files, data=data)

print(response.status_code)
print(response.json())

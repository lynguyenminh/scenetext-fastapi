import requests

url = 'http://0.0.0.0:8000/ocr/yolo_parseq/'
files = {'file': open('test-case.jpg', 'rb')}

response = requests.post(url, files=files)

print(response.status_code)
print(response.json())

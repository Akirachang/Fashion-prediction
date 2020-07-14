import requests

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'

data = {'file': open('/Users/akirachang/Desktop/YK800-92X-001_1.jpg', 'rb'), 'modelId': ('', 'f6ea04d4-f904-46cd-976e-825cada0f2cc')}

response = requests.post(url, auth= requests.auth.HTTPBasicAuth('D3_uJ_5iETUH3pO5pUid0ZkZdF24Iaa5', ''), files=data)

print(response.text)
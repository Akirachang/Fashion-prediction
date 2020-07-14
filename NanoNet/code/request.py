import requests

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/'

headers = {
  'accept': 'application/x-www-form-urlencoded'
}

data = {'modelId': 'f6ea04d4-f904-46cd-976e-825cada0f2cc', 'urls' : ['https://goo.gl/ICoiHc']}

response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth('D3_uJ_5iETUH3pO5pUid0ZkZdF24Iaa5', ''), data=data)

print(response.text)
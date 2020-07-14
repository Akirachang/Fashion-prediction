import requests

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/'

headers = {
  'accept': 'application/x-www-form-urlencoded'
}

data = {'modelId': 'f6ea04d4-f904-46cd-976e-825cada0f2cc', 'urls' : ['https://picture-fashion.oss-cn-beijing.aliyuncs.com/10000.jpg?Expires=1594703735&OSSAccessKeyId=TMP.3KjsEG2gnwTNfsF12ee4B5Rjph9fgjk34qFsEKk5x2vSWkGabKPY8wacMxHDpj43bxx2kK4SZGqsb1PPVssyfqPCH5QRzp&Signature=yDrnA9Bb3A5u%2BJBLHUTqgCkfPrQ%3D']}

response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth('D3_uJ_5iETUH3pO5pUid0ZkZdF24Iaa5', ''), data=data)

print(response.text)
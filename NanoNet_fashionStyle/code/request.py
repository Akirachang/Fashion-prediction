import requests

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/'

headers = {
  'accept': 'application/x-www-form-urlencoded'
}

data = {'modelId': 'f6ea04d4-f904-46cd-976e-825cada0f2cc', 'urls' : ['https://picture-fashion.oss-cn-beijing.aliyuncs.com/10007.jpg?Expires=1594261487&OSSAccessKeyId=TMP.3KgTbGh26S9P619iSEfKNx15qQdbgAiDASyx4QUcikQgKMLdPvEsmGQtLyZcvDveCPbLMovNuiRYtKbCc9ZahfUSzKCBWS&Signature=j1bTevoXPAbcUb%2BUlAFWSGeueC8%3D']}

response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth('D3_uJ_5iETUH3pO5pUid0ZkZdF24Iaa5', ''), data=data)

print(response.text)
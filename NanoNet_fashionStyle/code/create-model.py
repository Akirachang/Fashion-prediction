import requests, os, json, sys

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
url = BASE_URL + "Model/"

categories = ["OL风服装","中性风服装", "可爱系服装", "嘻哈风服装", "学院风服装", "朋克风服装", "欧美风服装", "民族风服装", "洛丽塔风服装", "淑女系服装", "田园风服装","百搭系服装","简约风服装","街头风服装","通勤风服装","韩版系服装"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG"]

data = {'categories' : categories}
headers = {
        'accept': 'application/x-www-form-urlencoded'
    }

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), data=data)
result = json.loads(response.text)
if not("model_id" in result.keys()):
    print('Error')
    print(result)
    sys.exit(1)
model_id = result["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")

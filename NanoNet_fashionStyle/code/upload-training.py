import os, requests

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/'
url = BASE_URL + 'UploadFile/'
categories = ["OL风服装","中性风服装", "可爱系服装", "嘻哈风服装", "学院风服装", "朋克风服装", "欧美风服装", "民族风服装", "洛丽塔风服装", "淑女系服装", "田园风服装","百搭系服装","简约风服装","街头风服装","通勤风服装","韩版系服装"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG"]
image_folder_path = "./images/train/"

model_id = os.environ.get('NANONETS_MODEL_ID')
AUTH_KEY = os.environ.get('NANONETS_API_KEY')

for category in categories:        
    class_image_path = os.path.join(image_folder_path, category)    
    all_class_images = [os.path.join(class_image_path, x) for x in os.listdir(class_image_path) if x.endswith(tuple(ext))]        
    for image in all_class_images:
        print (image)
        data = {'file' :open(image, 'rb'), 'category' :('', category), 'modelId' :('', model_id)}
        response = requests.post(url, auth= requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
        if response.status_code > 250 or response.status_code<200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")


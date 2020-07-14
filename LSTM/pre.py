import os
import requests
import pandas as pd

url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
columns = ['id', 'gender', 'year', 'major_type', 'major_color', 'style']


def get_feature(modelId, img_path):
    data = {'file': open(img_path, 'rb'),
            'modelId': ('', modelId)}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('D3_uJ_5iETUH3pO5pUid0ZkZdF24Iaa5', ''), files=data)
    return response.json()['result'][0]['prediction'][0]['label']


def get_picture():
    df = pd.DataFrame(columns=columns)
    path = 'images/'
    dirs = os.listdir(path)
    count = 0
    for row in range(load_csv.shape[0]):
        tmp_line = {}
        img = str(load_csv.loc[row, 'id']) + '.jpg'
        if img in dirs:
            img_path = path + img
            tmp_line['id'] = load_csv.loc[row, 'id']
            tmp_line['gender'] = load_csv.loc[row, 'gender']
            tmp_line['year'] = load_csv.loc[row, 'year']
            tmp_line['major_type'] = load_csv.loc[row, 'articleType']
            tmp_line['major_color'] = load_csv.loc[row, 'baseColour']
            # tmp_line['style'] = get_feature('f6ea04d4-f904-46cd-976e-825cada0f2cc', img_path)
        df = df.append(tmp_line, ignore_index=True)
        print(count)
        count += 1
    return df


if __name__ == '__main__':
    load_csv = pd.read_csv('styles.csv', error_bad_lines=False)
    output = get_picture()
    output.to_csv('df.csv', index_label='index')


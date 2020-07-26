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
    file = open('37000-40000.txt', 'w')#1
    for row in range(34000, 37000):#2
        tmp_line = {}
        img = str(load_csv.loc[row, 'id']) + '.jpg'
        if img in dirs:
            img_path = path + img
            # tmp_line['id'] = load_csv.loc[row, 'id']
            # tmp_line['gender'] = load_csv.loc[row, 'gender']
            # tmp_line['year'] = load_csv.loc[row, 'year']
            # tmp_line['major_type'] = load_csv.loc[row, 'articleType']
            # tmp_line['major_color'] = load_csv.loc[row, 'baseColour']
            try:
                tmp_line['style'] = get_feature('30bc8f97-7fac-4567-a287-b64acb990792', img_path)
                file.write(str(tmp_line['style']) + '\n')
            except:
                file.write('\n')
                print('an error occured!')
            print("saved!")
        df = df.append(tmp_line, ignore_index=True)
        print(count)
        count += 1
    return df


if __name__ == '__main__':
    load_csv = pd.read_csv('styles.csv', error_bad_lines=False)
    print(load_csv.shape[0])
    output = get_picture()
    output.to_csv('df.csv', index_label='index')


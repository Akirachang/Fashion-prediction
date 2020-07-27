import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

def create_dataset(dataset, look_back):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return np.array(dataX), np.array(dataY)


def load_csv():
    read_csv = pd.read_csv('csv/df.csv', encoding='gbk')
    return read_csv


def extract(csv, index, feature, child_feature, country, time=[2009, 2018]):
    res = {}
    s_time = time[0]
    e_time = time[1]
    for i in range(s_time, e_time+1):
        res[i] = 0
    if index == 1:
        for index in csv.loc[(csv['year'] <= e_time) & (csv['year'] >= s_time) & (csv[feature[0]] == child_feature[0])].index:
            if country == csv.loc[index, 'country']:
                year = int(csv.loc[index, 'year'])
                res[year] += 1
    elif index == 2:
        for index in csv.loc[(csv['year'] <= e_time) & (csv['year'] >= s_time) & (csv[feature[0]] == child_feature[0]) &
                            (csv[feature[1]] == child_feature[1])].index:
            if country == csv.loc[index, 'country']:
                year = int(csv.loc[index, 'year'])
                res[year] += 1
    elif index == 3:
        for index in csv.loc[(csv['year'] <= e_time) & (csv['year'] >= s_time) & (csv[feature[0]] == child_feature[0]) &
                            (csv[feature[1]] == child_feature[1]) & (csv[feature[2]] == child_feature[2])].index:
            if country == csv.loc[index, 'country']:
                year = int(csv.loc[index, 'year'])
                res[year] += 1
    print(res)
    return res


def LS(train_data, train_model, train_time=[2009, 2019]):
    all_list = []

    for i in range(train_time[1] - train_time[0] + 1):
        if train_model == 'month_model':
            for month in range(1, 13):
                if month in train_data[train_time[0] + i]:
                    all_list.append(train_data[train_time[0] + i][month])
        elif train_model == 'year_model':
            try:
                all_list.append(train_data[train_time[0] + i])
            except KeyError:
                all_list.append(0)

    all_list = np.array(all_list)
    all_list = all_list.reshape(len(all_list), 1)

    all_list = all_list.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    all_list = scaler.fit_transform(all_list)


    look_back = 1
    trainX, trainY = create_dataset(all_list, look_back)

    trainX = np.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))

    model = Sequential()
    model.add(LSTM(4, input_shape=(None, 1)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=50, batch_size=1, verbose=2)

    for i in range(1):
        tmp = (trainX[-1] + trainX[-2]) / 2
        trainX = np.append(trainX, np.expand_dims(tmp, 0))
        trainX = trainX.reshape((len(trainX), 1, 1))
    trainPredict = model.predict(trainX)
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform(trainY)


    x_value = []
    if train_model == 'month_model':
        plt.xlabel('month')
        """
            convert vector
        """
    elif train_model == 'year_model':
        plt.xlabel('year')
        # x_value = train_time + [train_time[-1]+1]
    """
    draw pic
    """
    # plt.ylabel('count')
    # plt.plot(trainY)    # correct results
    # plt.plot(trainPredict[1:])  # predicted results
    # plt.show()

    return int(trainPredict.tolist()[-1][0])  # return predict result


def country_csv_write(country_output):
    df = pd.DataFrame(columns=['State', 'Unemployment'])
    for line in country_output:
        print(line)
        df = df.append(line, ignore_index=True)
    df.to_csv('csv/fashion_statistic.csv')


def entrance(majorType, majorColor):
    model = 'LSTM'
    csv = load_csv()
    countries = ['Afghanistan','Angola','Albania','United Arab Emirates','Argentina','Armenia','Antarctica','French Southern and Antarctic Lands','Australia','Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria','The Bahamas','Bosnia and Herzegovina','Belarus','Belize','Bolivia','Brazil','Brunei','Bhutan','Botswana','Central African Republic','Canada','Switzerland','Chile','China','Ivory Coast','Cameroon','Democratic Republic of the Congo','Republic of the Congo','Colombia','Costa Rica','Cuba','Northern Cyprus','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Eritrea','Spain','Estonia','Ethiopia','Finland','Fiji','Falkland Islands','France','Gabon','United Kingdom','Georgia','Ghana','Guinea','Gambia','Guinea Bissau','Equatorial Guinea','Greece','Greenland','Guatemala','Guyana','Honduras','Croatia','Haiti','Hungary','Indonesia','India','Ireland','Iran','Iraq','Iceland','Israel','Italy','Jamaica','Jordan','Japan','Kazakhstan','Kenya','Kyrgyzstan','Cambodia','South Korea','Kosovo','Kuwait','Laos','Lebanon','Liberia','Libya','Sri Lanka','Lesotho','Lithuania','Luxembourg','Latvia','Morocco','Moldova','Madagascar','Mexico','Macedonia','Mali','Myanmar','Montenegro','Mongolia','Mozambique','Mauritania','Malawi','Malaysia','Namibia','New Caledonia','Niger','Nigeria','Nicaragua','Netherlands','Norway','Nepal','New Zealand','Oman','Pakistan','Panama','Peru','Philippines','Papua New Guinea','Poland','Puerto Rico','North Korea','Portugal','Paraguay','Qatar','Romania','Russia','Rwanda','Western Sahara','Saudi Arabia','Sudan','South Sudan','Senegal','Solomon Islands','Sierra Leone','El Salvador','Somaliland','Somalia','Republic of Serbia','Suriname','Slovakia','Slovenia','Sweden','Swaziland','Syria','Chad','Togo','Thailand','Tajikistan','Turkmenistan','East Timor','Trinidad and Tobago','Tunisia','Turkey','Taiwan','United Republic of Tanzania','Uganda','Ukraine','Uruguay','United States of America','Uzbekistan','Venezuela','Vietnam','Vanuatu','West Bank','Yemen','South Africa','Zambia','Zimbabwe']
    main_countries = ['China', 'Thailand', 'america', 'Japan', 'Korea', 'singapore', 'France', 'Germany',
                'Italy', 'England', 'Canada', 'Russia', 'Brazil', 'Mexico', 'Australia']
    if model == 'LSTM':
        country_output = []
        for country in countries:
            if country in main_countries: 
                country_dict = {}
                train_data = extract(csv, 2, ['major_type', 'major_color'], [majorType, majorColor], country, time=[2009, 2018])
                res_predict = LS(train_data, 'year_model', train_time=[2011, 2018])
                country_dict['State'] = country
                country_dict['Unemployment'] = res_predict
                country_output.append(country_dict)
            else:
                country_dict = {}
                country_dict['State'] = country
                country_dict['Unemployment'] = 0
                country_output.append(country_dict)
        country_csv_write(country_output)

def entrance_2(majorType, style):
    model = 'LSTM'
    csv = load_csv()
    countries = ['Afghanistan','Angola','Albania','United Arab Emirates','Argentina','Armenia','Antarctica','French Southern and Antarctic Lands','Australia','Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria','The Bahamas','Bosnia and Herzegovina','Belarus','Belize','Bolivia','Brazil','Brunei','Bhutan','Botswana','Central African Republic','Canada','Switzerland','Chile','China','Ivory Coast','Cameroon','Democratic Republic of the Congo','Republic of the Congo','Colombia','Costa Rica','Cuba','Northern Cyprus','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Eritrea','Spain','Estonia','Ethiopia','Finland','Fiji','Falkland Islands','France','Gabon','United Kingdom','Georgia','Ghana','Guinea','Gambia','Guinea Bissau','Equatorial Guinea','Greece','Greenland','Guatemala','Guyana','Honduras','Croatia','Haiti','Hungary','Indonesia','India','Ireland','Iran','Iraq','Iceland','Israel','Italy','Jamaica','Jordan','Japan','Kazakhstan','Kenya','Kyrgyzstan','Cambodia','South Korea','Kosovo','Kuwait','Laos','Lebanon','Liberia','Libya','Sri Lanka','Lesotho','Lithuania','Luxembourg','Latvia','Morocco','Moldova','Madagascar','Mexico','Macedonia','Mali','Myanmar','Montenegro','Mongolia','Mozambique','Mauritania','Malawi','Malaysia','Namibia','New Caledonia','Niger','Nigeria','Nicaragua','Netherlands','Norway','Nepal','New Zealand','Oman','Pakistan','Panama','Peru','Philippines','Papua New Guinea','Poland','Puerto Rico','North Korea','Portugal','Paraguay','Qatar','Romania','Russia','Rwanda','Western Sahara','Saudi Arabia','Sudan','South Sudan','Senegal','Solomon Islands','Sierra Leone','El Salvador','Somaliland','Somalia','Republic of Serbia','Suriname','Slovakia','Slovenia','Sweden','Swaziland','Syria','Chad','Togo','Thailand','Tajikistan','Turkmenistan','East Timor','Trinidad and Tobago','Tunisia','Turkey','Taiwan','United Republic of Tanzania','Uganda','Ukraine','Uruguay','United States of America','Uzbekistan','Venezuela','Vietnam','Vanuatu','West Bank','Yemen','South Africa','Zambia','Zimbabwe']
    main_countries = ['China', 'Thailand', 'america', 'Japan', 'Korea', 'singapore', 'France', 'Germany',
                'Italy', 'England', 'Canada', 'Russia', 'Brazil', 'Mexico', 'Australia']
    if model == 'LSTM':
        country_output = []
        for country in countries:
            if country in main_countries: 
                country_dict = {}
                train_data = extract(csv, 2, ['major_type', 'style'], [majorType, style], country, time=[2009, 2018])
                res_predict = LS(train_data, 'year_model', train_time=[2011, 2018])
                country_dict['State'] = country
                country_dict['Unemployment'] = res_predict
                country_output.append(country_dict)
            else:
                country_dict = {}
                country_dict['State'] = country
                country_dict['Unemployment'] = 0
                country_output.append(country_dict)
        country_csv_write(country_output)

def entrance_3(majorColor, style):
    model = 'LSTM'
    csv = load_csv()
    countries = ['Afghanistan','Angola','Albania','United Arab Emirates','Argentina','Armenia','Antarctica','French Southern and Antarctic Lands','Australia','Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria','The Bahamas','Bosnia and Herzegovina','Belarus','Belize','Bolivia','Brazil','Brunei','Bhutan','Botswana','Central African Republic','Canada','Switzerland','Chile','China','Ivory Coast','Cameroon','Democratic Republic of the Congo','Republic of the Congo','Colombia','Costa Rica','Cuba','Northern Cyprus','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Eritrea','Spain','Estonia','Ethiopia','Finland','Fiji','Falkland Islands','France','Gabon','United Kingdom','Georgia','Ghana','Guinea','Gambia','Guinea Bissau','Equatorial Guinea','Greece','Greenland','Guatemala','Guyana','Honduras','Croatia','Haiti','Hungary','Indonesia','India','Ireland','Iran','Iraq','Iceland','Israel','Italy','Jamaica','Jordan','Japan','Kazakhstan','Kenya','Kyrgyzstan','Cambodia','South Korea','Kosovo','Kuwait','Laos','Lebanon','Liberia','Libya','Sri Lanka','Lesotho','Lithuania','Luxembourg','Latvia','Morocco','Moldova','Madagascar','Mexico','Macedonia','Mali','Myanmar','Montenegro','Mongolia','Mozambique','Mauritania','Malawi','Malaysia','Namibia','New Caledonia','Niger','Nigeria','Nicaragua','Netherlands','Norway','Nepal','New Zealand','Oman','Pakistan','Panama','Peru','Philippines','Papua New Guinea','Poland','Puerto Rico','North Korea','Portugal','Paraguay','Qatar','Romania','Russia','Rwanda','Western Sahara','Saudi Arabia','Sudan','South Sudan','Senegal','Solomon Islands','Sierra Leone','El Salvador','Somaliland','Somalia','Republic of Serbia','Suriname','Slovakia','Slovenia','Sweden','Swaziland','Syria','Chad','Togo','Thailand','Tajikistan','Turkmenistan','East Timor','Trinidad and Tobago','Tunisia','Turkey','Taiwan','United Republic of Tanzania','Uganda','Ukraine','Uruguay','United States of America','Uzbekistan','Venezuela','Vietnam','Vanuatu','West Bank','Yemen','South Africa','Zambia','Zimbabwe']
    main_countries = ['China', 'Thailand', 'america', 'Japan', 'Korea', 'singapore', 'France', 'Germany',
                'Italy', 'England', 'Canada', 'Russia', 'Brazil', 'Mexico', 'Australia']
    if model == 'LSTM':
        country_output = []
        for country in countries:
            if country in main_countries: 
                country_dict = {}
                train_data = extract(csv, 2, ['major_color', 'style'], [majorColor, style], country, time=[2009, 2018])
                res_predict = LS(train_data, 'year_model', train_time=[2011, 2018])
                country_dict['State'] = country
                country_dict['Unemployment'] = res_predict
                country_output.append(country_dict)
            else:
                country_dict = {}
                country_dict['State'] = country
                country_dict['Unemployment'] = 0
                country_output.append(country_dict)
        country_csv_write(country_output)
    
def entrance_4(majorColor, majorType ,style):
    model = 'LSTM'
    csv = load_csv()
    countries = ['Afghanistan','Angola','Albania','United Arab Emirates','Argentina','Armenia','Antarctica','French Southern and Antarctic Lands','Australia','Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria','The Bahamas','Bosnia and Herzegovina','Belarus','Belize','Bolivia','Brazil','Brunei','Bhutan','Botswana','Central African Republic','Canada','Switzerland','Chile','China','Ivory Coast','Cameroon','Democratic Republic of the Congo','Republic of the Congo','Colombia','Costa Rica','Cuba','Northern Cyprus','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Eritrea','Spain','Estonia','Ethiopia','Finland','Fiji','Falkland Islands','France','Gabon','United Kingdom','Georgia','Ghana','Guinea','Gambia','Guinea Bissau','Equatorial Guinea','Greece','Greenland','Guatemala','Guyana','Honduras','Croatia','Haiti','Hungary','Indonesia','India','Ireland','Iran','Iraq','Iceland','Israel','Italy','Jamaica','Jordan','Japan','Kazakhstan','Kenya','Kyrgyzstan','Cambodia','South Korea','Kosovo','Kuwait','Laos','Lebanon','Liberia','Libya','Sri Lanka','Lesotho','Lithuania','Luxembourg','Latvia','Morocco','Moldova','Madagascar','Mexico','Macedonia','Mali','Myanmar','Montenegro','Mongolia','Mozambique','Mauritania','Malawi','Malaysia','Namibia','New Caledonia','Niger','Nigeria','Nicaragua','Netherlands','Norway','Nepal','New Zealand','Oman','Pakistan','Panama','Peru','Philippines','Papua New Guinea','Poland','Puerto Rico','North Korea','Portugal','Paraguay','Qatar','Romania','Russia','Rwanda','Western Sahara','Saudi Arabia','Sudan','South Sudan','Senegal','Solomon Islands','Sierra Leone','El Salvador','Somaliland','Somalia','Republic of Serbia','Suriname','Slovakia','Slovenia','Sweden','Swaziland','Syria','Chad','Togo','Thailand','Tajikistan','Turkmenistan','East Timor','Trinidad and Tobago','Tunisia','Turkey','Taiwan','United Republic of Tanzania','Uganda','Ukraine','Uruguay','United States of America','Uzbekistan','Venezuela','Vietnam','Vanuatu','West Bank','Yemen','South Africa','Zambia','Zimbabwe']
    main_countries = ['China', 'Thailand', 'america', 'Japan', 'Korea', 'singapore', 'France', 'Germany',
                'Italy', 'England', 'Canada', 'Russia', 'Brazil', 'Mexico', 'Australia']
    if model == 'LSTM':
        country_output = []
        for country in countries:
            if country in main_countries: 
                country_dict = {}
                train_data = extract(csv, 3, ['major_color', 'major_type','style'], [majorColor, majorType, style], country, time=[2009, 2018])
                res_predict = LS(train_data, 'year_model', train_time=[2011, 2018])
                country_dict['State'] = country
                country_dict['Unemployment'] = res_predict
                country_output.append(country_dict)
            else:
                country_dict = {}
                country_dict['State'] = country
                country_dict['Unemployment'] = 0
                country_output.append(country_dict)
        country_csv_write(country_output)
    
# if __name__ == '__main__':
#     entrance(majorType, majorColor)


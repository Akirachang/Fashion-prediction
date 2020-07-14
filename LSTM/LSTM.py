import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler



dict_place = {'Bangkok': 1, 'Beijing': 2, 'Bogota': 3, 'Buenos Aires': 4, 'Cairo': 5, 'Delhi': 6, 'Dhaka': 7,
              'Guangzhou': 8, 'Istanbul': 9, 'Jakarta': 10, 'Karachi': 11, 'Kolkata': 12, 'Lagos': 13, 'London': 14,
              'Los Angeles': 15, 'Manila': 16, 'Mexico City': 17, 'Mumbai': 18, 'New York': 19, 'Osaka': 20, 'Rio de Janeiro': 21,
              'Sao Paulo': 22, 'Seoul': 23, 'Shanghai': 24, 'Tianjin': 25, 'Tokyo': 26, 'Paris': 27, 'Berlin': 28,
              'Madrid': 29, 'Kiev': 30, 'Rome': 31, 'Budapest': 32, 'Milan': 33, 'Sofia': 34, 'Nairobi': 35,
              'Sydney': 36, 'Moscow': 37, 'Johannesburg': 38, 'Toronto': 39, 'Vancouver': 40, 'Chicago': 41, 'Austin': 42,
              'Seattle': 43, 'Singapore': 44, 'world-wide': 45}


def create_dataset(dataset, look_back):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return np.array(dataX),np.array(dataY)


def load_csv():
    read_csv = pd.read_csv('df.csv')
    return read_csv


def extract(csv, city, feature, child_feature, time=[2009, 2019]):
    res = {}
    city_id = dict_place[city]
    s_time = time[0]
    e_time = time[1]
    for index in csv.loc[(csv['year'] <= e_time) & (csv['year'] >= s_time) & (csv[feature] == child_feature)].index:
        # if city_id > 44 or city_id == csv.loc[index, 'city_id']:
        if city_id > 44:
            year = int(csv.loc[index, 'year'])
            # month = csv.loc[index, 'month']
            if year not in res:
                res[year] = 1
            else:
                res[year] += 1
            # else:
            #     if month not in res[year]:
            #         res[year][month] = 1
            #     else:
            #         res[year][month] += 1
    print(res)
    return res


def LS(train_data, train_model, train_time=[2013, 2015], test_time=[2015, 2015]):
    all_list = []

    for i in range(train_time[1] - train_time[0] + 1):
        if train_model == 'month_model':
            for month in range(1, 13):
                if month in train_data[train_time[0] + i]:
                    all_list.append(train_data[train_time[0] + i][month])
        elif train_model == 'year_model':
            all_list.append(train_data[train_time[0] + i])


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

    for i in range(2):
        # tmp = (trainX[-1] + trainX[-2] + trainX[-13] + trainX[-14]) / 4
        tmp = (trainX[-1] + trainX[-2]) / 2
        trainX = np.append(trainX, np.expand_dims(tmp, 0))
        trainX = trainX.reshape((len(trainX), 1, 1))
    # print(trainX)
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
            convert vector
        """
    plt.ylabel('count')
    plt.plot(trainY)    # correct results
    plt.plot(trainPredict[1:])  # predicted results
    plt.show()


def entrance():
    model = 'LSTM'
    csv = load_csv()
    train_data = extract(csv, 'world-wide', 'major_type', 'Bra', time=[2009, 2019])
    if model == 'LSTM':
        LS(train_data, 'year_model', train_time=[2011, 2018])


if __name__ == '__main__':
    entrance()


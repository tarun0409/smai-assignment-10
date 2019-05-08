import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import SimpleRNN
from keras.layers import Dense,Flatten

data = pd.read_csv('GoogleStocks.csv')

low_arr = data['low'].values
high_arr = data['high'].values
avg_arr = (low_arr + high_arr)/2
data['avg'] = avg_arr

data_train, data_test, out_train, out_test = train_test_split(
    data[['volume','avg']],
    data[['open']],
    test_size=0.2,
    random_state=0)

out_train_arr = out_train[['open']].values
out_test_arr = out_test[['open']].values
train_ts = data_train[['volume','avg']].values
test_ts = data_test[['volume','avg']].values
sc = MinMaxScaler(feature_range=(0,1))
sc.fit(train_ts)
train_ts_scaled = sc.transform(train_ts)
test_ts_scaled = sc.transform(test_ts)
scy = MinMaxScaler(feature_range=(0,1))
scy.fit(out_train_arr)
out_train_scaled = scy.transform(out_train_arr)
out_test_scaled = scy.transform(out_test_arr)


H = [2,3]
C = [30,50,80]
T = [20,50,75]
n = 1
for h in H:
    for c in C:
        e = 50
        for t in T:
            print
            print '::::::::::::MODEL '+str(n)+' ::::::::::::::::'
            print 'Number of Hidden Layers : '+str(h)
            print 'Number of cells in Hidden Layers : '+str(c)
            print 'Number of Time Steps : '+str(t)
            print 'Number of Epochs : '+str(e)
            print
            X_train = []
            y_train = []
            X_test = []
            y_test = []
            for i in range(t, train_ts_scaled.shape[0]):
                X_train.append(train_ts_scaled[i-t:i, :])
                y_train.append(out_train_scaled[i, 0])
            X_train, y_train = np.array(X_train), np.array(y_train)
            for i in range(t, test_ts_scaled.shape[0]):
                X_test.append(test_ts_scaled[i-t:i, :])
                y_test.append(out_test_scaled[i, 0])
            X_test, y_test = np.array(X_test), np.array(y_test)
            model = Sequential()
            for m in range(0,h):
                model.add(SimpleRNN(units=c,return_sequences=True))
            model.add(Flatten())
            model.add(Dense(units = 1))
            model.compile(optimizer = 'adam', loss = 'mean_squared_error')
            model.fit(X_train, y_train, epochs = e, batch_size = 32)
            err = model.evaluate(X_test, y_test)
            print
            print 'Model '+str(n)+' error : '+str(err)
            print
            print '================================================================='
            e = e/2
            n += 1



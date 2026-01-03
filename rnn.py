import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras import layers

url = "https://raw.githubusercontent.com/mwitiderrick/stockprice/master/NSE-TATAGLOBAL.csv"
data = pd.read_csv(url)
print(data.head())

#Use a figure to visualize the stock price
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label=['Closing Price'])
plt.title('Stock Price Over Time')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()

#pre process the data - in this section we use the lstm to predict the next closing price
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))

#How many days to look at
lookback_days = 30
x, y = [], []

for i in range(lookback_days, len(scaled_data)):
  x.append(scaled_data[i - lookback_days:i, 0])
  y.append(scaled_data[i, 0])

x, y = np.array(x), np.array(y)
x = np.reshape(x, (x.shape[0], x.shape[1], 1)) #LSTM expects a 3D input so this reshapes it
#split the data into train and test
train_size = int(len(x) * 0.8)
x_train, x_test = x[:train_size], x[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

#build the LSTM model
model = keras.Sequential([
  layers.GRU(100, return_sequences=True, input_shape=(x_train.shape[-1], 1)),
  layers.GRU(100, return_sequences=False),#GATED RECURRING UNIT
  layers.Dense(25),
  layers.Dense(1)
])
model.compile(optimizer='RMSprop',
    loss=keras.losses.MeanSquaredError())

#TRAIN THE MODEL
model.fit(
  x_train,
  y_train,
  epochs=20,
  batch_size=32,
  validation_split=0.1
)

#Evaluate and predict
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

#Visualize the prediction
plt.figure(figsize=(10, 6))
plt.plot(y_test_actual, label='Actual Price')
plt.plot(predictions, label='Predicted Price')
plt.title('Stock Price Prediction')
plt.xlabel('Days')
plt.ylabel('Price')
plt.legend()
plt.show()
#Assi 3B
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal','Shirt', 'Sneaker', 'Bag', 'Ankleboot']

df1 = pd.read_csv(r'D:\DL Practicals\Dataset\fashion-mnist_train.csv')

df1

x_train = df1.drop("label", axis=1).values
y_train = df1["label"].values

print("x_train shape: ",x_train.shape)
print("y_train shape: ",y_train.shape)

np.unique(y_train)

df2 = pd.read_csv(r'D:\DL Practicals\Dataset\fashion-mnist_test.csv')

df2

x_test = df2.drop("label", axis=1).values
y_test = df2["label"].values

print("x_test shape: ",x_test.shape)
print("y_test shape: ",y_test.shape)

x_train = x_train.reshape(60000, 28, 28)
x_test = x_test.reshape(10000, 28, 28)

print(x_train[0])

y_train[0]

plt.imshow(x_train[0])

x_test[10]

y_test[10]

plt.imshow(x_test[10])

x_train = x_train/255
x_test = x_test/255

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

print("Train Shape :",x_train.shape)
print("Test Shape :",x_test.shape)
print("y_train shape :",y_train.shape)
print("y_test shape :",y_test.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

model=Sequential()
model.add(Conv2D(64, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=3, verbose=1,validation_data=(x_test,y_test))

predictions = model.predict(x_test)

import numpy as np
index=10
print(predictions[index])
final_value=np.argmax(predictions[index])
print("Actual label :",y_test[index])
print("Predicted label :",final_value)
print("Class :",class_names[final_value])

plt.imshow(x_test[10])


loss, accuracy = model.evaluate(x_test, y_test)
print("Loss :",loss)
print("Accuracy (Test Data) :",accuracy*100)

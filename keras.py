import os
import glob
import pandas as pd
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
#os.chdir(""/) #select our directory

extension = "csv"
all_filenames = [i for i in glob.glob('*x{}'.format(extension))]
combined_csv = pd.concat([pd.read+csv(f) for f in all_filenames])
combined_csv.tocsv("combined_csv.csv", index=False, encoding='utf-8-sig') #combine the csv files into one csv file

dataset = loadtxt(, delimeter)
X = dataset[:,0:5]
y = dataset[:,9]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='a'))
model.add(Dense(8, activation='a'))
model.add(Dense(1, activation='b'))
model.compile(loss='binaryCrossentropy', optimizer='c', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10) #fit model

accuracycheck = model.evaluate(X, y)
import numpy as np
import string
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

#file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"
modi_file = "/home/miberg/Desktop/NN/chopin_mod.krn"
alphabet_file = "/home/miberg/Desktop/NN/kern_alphabet.txt"


alphabet = []
for line in open(alphabet_file, "r").readlines():
    line = line.rstrip()
    alphabet.append(line)
alphabet.append('\\n')
alphabet.append('\\t')
alphabet.append('\\s')
print(alphabet)


raw = []
voc_map = {}
nvoc = 1
nsamp = 0
for line in open(file):
    nsamp += 1
    line = line.rstrip('\n')
    raw.append(line.split('\t'))
    for token in line.split('\t'):
        if not token in voc_map:
            voc_map.update({token: nvoc})
            nvoc += 1

encoded = []

maxa = 0
for i in range(len(raw)):
    a = 0
    tmp = []
    for token in raw[i]:
        tmp.append(voc_map.get(token))
        a = a + 1
    if a > maxa:
        maxa = a
    encoded.append(tmp)

padded = []
for row in encoded:
    tmp = np.pad(row, (0, maxa - len(row)), mode='constant', constant_values=0)
    padded.append(tmp)

seq_length = 100
dataX = []
dataY = []

for i in range(0, len(padded) - seq_length, 1):
    dataX.append(padded[i:i + seq_length])
    dataY.append(padded[i + seq_length])
    n_patterns = len(dataX)
print("Total number of training cases: " + str(n_patterns))

pass

X = np.reshape(dataX, (n_patterns, seq_length, maxa))
X = X / float(nvoc)

Y = []
for i in range(len(dataY)):
    tmp = []
    for token in dataY[i]:
        tmp.append(np_utils.to_categorical(dataY[i], nvoc))
    Y.append(tmp)

pass
pass

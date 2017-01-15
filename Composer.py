import numpy as np
import string
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"

raw = []
voc_map = {}
nvoc = 0
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

padded = np.empty((nsamp, maxa))
for row in encoded:
    tmp = np.array(np.pad(row, maxa))
    np.append(padded, tmp)




pass
import numpy
import string
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"

split_data = []
voc_map = {}
n = 0
for line in open(file):
    line = line.rstrip('\n')
    split_data.append(line.split('\t'))
    for token in line.split('\t'):
        if not token in voc_map:
            voc_map.update({token: n})
            n += 1


pass
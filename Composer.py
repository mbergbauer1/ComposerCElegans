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

for line in open(file):
    line = line.rstrip('\n')
    split_data.append(line.split('\t'))




raw_text = open(file).read()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)
pass
import numpy as np
import string
import re
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


#file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"
# modi_file = "/home/miberg/Desktop/NN/chopin_mod.krn"
# alphabet_file = "/home/miberg/Desktop/NN/kern_alphabet.txt"

# file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"
# modi_file = "/home/miberg/Desktop/NN/chopin_mod.krn"
alphabet_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\kern_alphabet.txt"
file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"

alphabet = []
for line in open(alphabet_file, "r").readlines():
    line = line.rstrip()
    alphabet.append(line)
alphabet.append('\\n')
alphabet.append('\\t')
alphabet.append('\\s')

raw = []
voc_map = {}
nvoc = 1


for line in open(file):
    raw.append(tokenize(line))


def tokenize(line):
    tmp = line

    return tokens

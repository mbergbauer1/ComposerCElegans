import numpy as np
import string
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


#alphabet_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\kern_alphabet.txt"
#file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"

alphabet_file = "C:\\Users\\bergbmi\\Desktop\\NN\\KernFiles\\kern_alphabet.txt"
file = "C:\\Users\\bergbmi\\Desktop\\NN\\KernFiles\\chopin_mod.krn"


def createAlphabet(file):
    tmp = []
    for line in open(alphabet_file, "r").readlines():
        line = line.rstrip()
        tmp.append(line)
    tmp.append('%') # \\t
    tmp.append('@') # \\n
    tmp.append('+') # \\s
    return tmp

def find_all_pos(str,substr):
    n = 0
    while True:
        n = str.find(substr,n)
        if n == -1: return
        yield n
        n += len(substr)

def tokenize(line):
    tokens_in_line = []
    positions_of_tokens = []
    line = line.replace("\t","%")
    line = line.replace("\n","@")
    line = line.replace("\s","+")
    origline = line
    for token in alphabet:
        while token in line:
            pos = line.find(token)
            tokens_in_line.append(token)
            a = line[:pos]
            b = line[pos+len(token):]
            line = a + b
    unique_tokens_in_line = list(set(tokens_in_line))
    tokens_with_position = {}
    for token in unique_tokens_in_line:
        #positions_of_tokens.append(list(find_all_pos(origline, token)))
        tmp = list(find_all_pos(origline,token))
        for pos in tmp:
            tokens_with_position.update({pos:str(token)})
    ordered_tokens_in_line = []
    for k, v in sorted(tokens_with_position.items()):
        ordered_tokens_in_line.append(v)

    return ordered_tokens_in_line

raw = []
voc_map = {}
nvoc = 1
alphabet = createAlphabet(alphabet_file)
for line in open(file):
    raw.append(tokenize(line))
pass



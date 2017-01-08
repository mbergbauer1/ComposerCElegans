

from keras.utils import np_utils

orig_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin.krn"
modi_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"
f_orig = open(orig_file,"r")
lines = f_orig.readlines()
f_orig.close()

f_mod = open(modi_file,"w")

for line in lines:
    line = line.translate(str.maketrans('', '', 'XYZ@%+|<>'))
    if line[0] == '!':
        continue
    elif line[0] == '*':
        continue
    else:
        f_mod.write(line)


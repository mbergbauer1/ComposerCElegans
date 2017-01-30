from keras.utils import np_utils

orig_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin.krn"
modi_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"
#alphabet_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\kern_alphabet.txt"


# orig_file = "C:\\Users\\bergbmi\\Desktop\\NN\\KernFiles\\chopin.krn"
# modi_file = "C:\\Users\\bergbmi\\Desktop\\NN\\KernFiles\\chopin_mod.krn"

#alphabet_file = "/home/miberg/Desktop/NN/kern_alphabet.txt"


f_orig = open(orig_file, "r")
lines = f_orig.readlines()
f_orig.close()

f_mod = open(modi_file, "w")

total_t = 0
for line in lines:
    line = line.translate(str.maketrans('', '', 'XYZxyz@%+|<>'))
    if line[0] == '!':
        continue
    elif line[0] == '*':
        continue
    else:
        f_mod.write(line)



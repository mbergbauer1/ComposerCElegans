

from keras.utils import np_utils

orig_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin.krn"
modi_file = "C:\\Users\\mbergbauer\\Desktop\\NN\\KernFiles\\chopin_mod.krn"
f_orig = open(orig_file,"r")
lines = f_orig.readlines()
f_orig.close()

f_mod = open(modi_file,"w")
vocabulary = []

total_t = 0
for line in lines:
    line = line.translate(str.maketrans('', '', 'XYZ@%+|<>'))
    if line[0] == '!':
        continue
    elif line[0] == '*':
        continue
    else:

        f_mod.write(line)

        for token in line.split('\t'):
            total_t += 1
            token = token.rstrip()
            if not token in vocabulary:
                vocabulary.append(token)

total_v = 0
for x in vocabulary:
    total_v += 1

print('Number of tokens in file: ' + str(total_t))
print('Vocabulary in file: ' + str(total_v))
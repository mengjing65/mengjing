import pandas as pd
import numpy as np

data = pd.read_table('yq_in.txt', sep='\t', header=None)
py_in = data.values
inset = np.array(py_in)
file = open('D:/Desktop/test/yq_out.txt', 'a')
count = inset.shape[0]

for x in range(count):
    if inset[x][0] != inset[x-1][0]:
        file.write('%s\n' % inset[x][0])
        file.write('%s\t' % inset[x][1])
        file.write('%d\n' % inset[x][2])
    else:
        file.write('%s\t' % inset[x][1])
        file.write('%d\n' % inset[x][2])

#
# read binary file (tuple)
# and print it
#
import pickle

with open('tupla.bin','rb') as fh:
        t = pickle.load(fh) 

print(type(t))
print(t)

print('done...')

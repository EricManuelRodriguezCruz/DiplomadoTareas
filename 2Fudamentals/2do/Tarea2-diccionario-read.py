#
# read binary file (dictionary)
# and print it
#
import pickle

with open('Diccionario.bin','rb') as fh:
        d = pickle.load(fh) 

print(type(d))
print(d)

print('done...')

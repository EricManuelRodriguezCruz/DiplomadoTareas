#
# 2do
#
import pickle
d={}
d={'hecho por':'Erick MAnuel Rodriguez Cruz','El dia':'1-05-2022'}

with open('Diccionario.bin','wb') as fh:
        pickle.dump(d,fh)

print('done...')

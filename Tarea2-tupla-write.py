#
# 2do
#
import pickle
t=()
t=12,True,3.1,'aCat','hecho por','Erick MAnuel Rodriguez Cruz','El dia','1-05-2022'

with open('tupla.bin','wb') as fh:
        pickle.dump(t,fh)

print('done...')

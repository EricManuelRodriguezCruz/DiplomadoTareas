#
# radious of circle inscribed in a tringle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\ercru>python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> a=9
>>> b=7
>>> c=4
>>> semip=(a+b+c)/2
>>> suma=(semip*(semip-a)*(semip-b)*(semip-c)
... )
>>> raiz=math.sqrt(suma)
>>> resultado=raiz/semip
>>> print(resultado)
1.3416407864998738
>>>

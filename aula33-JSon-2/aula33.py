import json
from textwrap import indent

from numpy import identity

carros_dictionary={
    "marca":"honda",
    "modelo":"HRV",
    "cor":"prata"
}

#dictionary -> objeto json

carros_list=["honda","HRV","prata","ford","fiat","chevrolet"]
#list -> array json

carros_tupla=("honda","HRV","prata","ford","fiat","chevrolet")
#tupla -> array json

carros_j_d=json.dumps(carros_dictionary,indent=4,separators=(":","="),sort_keys=True)
carros_j_l=json.dumps(carros_list)
carros_j_t=json.dumps(carros_tupla)

#indent = identação do jason
#separators=(":","=") = formatar separador
#sort_keys=True = ordem alfabetica das chaves

print(carros_j_d)
print("-----------------------")
print(carros_j_l)
print("-----------------------")
print(carros_j_t)


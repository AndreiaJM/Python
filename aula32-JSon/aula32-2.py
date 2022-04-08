import json
import os

#tranformando divtionary para json
carros={"marca":"honda","modelo":"HRV","cor":"prata"}

#convertendo o divtionary em json
carros_json=json.dumps(carros)

print(carros_json)


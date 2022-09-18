# JSON: JavaScript Object Notation
# File format

# python native

import json

data = {'name': 'kamyar',
        'surname': 'Mazaheri Fard',
        'gender': 'male',
        'age': 30}
# .dumps():
j_data = json.dumps(data)  # it returns a json data format that is string
print(type(j_data))
print(j_data)
# .dump(): it write json to a file
with open('j_file.json', 'w') as jf:
    json.dump(data, jf)
















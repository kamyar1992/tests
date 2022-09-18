# REST API
# free APIs:
# 1. https://randomuser.me/
# 2. dog api
# 3. cat api

import requests

response = requests.get('https://randomuser.me/api/?nat=ir')
print(response)  # it prints HTTP code 200, that means the response is ok
print(response.text)












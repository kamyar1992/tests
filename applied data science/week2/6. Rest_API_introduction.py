# REST API
# free APIs:
# 1. https://randomuser.me/
# 2. dog api
# 3. cat api

import requests

response = requests.get('https://randomuser.me/api/?nat=ir')
print(response)  # it prints HTTP code 200, that means the response is ok


base_url = 'https://randomuser.me'
end_poit = 'api/?nat=ir'

# query_parameters : it starts with ?

# HTTP(s) : (response) status codes : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# status codes have range:
# Informational responses (100–199)
# Successful responses (200–299)
# Redirection messages (300–399)
# Client error responses (400–499)
# Server error responses (500–599)

# HTTP methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
# .content: returns binary result of the .get()
print('='*20, 'text vs content', '='*20)
print(response.content)
print(response.text)

print('='*20, 'status code & reason', '='*20)
print(response.status_code)
print(response.reason)

print('='*20, 'http headers', '='*20)
print(response.headers)

print('='*20, 'request properties', '='*20)
req = response.request
print(req.headers)
print(req.path_url)
print(req.url)
print(req.method)







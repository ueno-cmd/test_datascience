import json
import requests

response = requests.post(
    'http://127.0.0.1:5000/predict',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'data': [[2.0, 164.0, 1.0, 1.0, 0.0, 1.0, 3.0, 0.0, 0.0, 99.4, 176.6, 66.4, 54.3, 2824.0, 3.0, 1.0, 136.0, 5.0, 3.19, 3.4, 8.0, 115.0, 5500.0, 18.0, 22.0]]})
)
result = response.json()
print(json.dumps(result, indent=4))

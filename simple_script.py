import requests

response = requests.get(
    'http://geojson.io/#map=18/52.52060/31.18780'
)
print(response.text)

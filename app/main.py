import requests

print("Hello, World!")
url="https://api.carbonintensity.org.uk/intensity"
response = requests.get(url)
print(response.json())
import requests

site = "https://ifconfig.co/ip"
response = requests.get(url=site)

print(f"Codigo HTTP: {response.status_code}")
print(f"Meu endereço IP: {response.text}")

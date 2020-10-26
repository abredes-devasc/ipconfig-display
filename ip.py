import requests

site = "https://ifconfig.co/ip"
response = requests.get(url=site)

print(f"Codigo HTTP: {response.status_code}")
print(f"Meu endereço IP: {response.text}")

site = "https://ifconfig.co/asn"
response = requests.get(url=site)
print(f"Codigo HTTP: {response.status_code}")
print(f"Meu ASN: {response.text}")

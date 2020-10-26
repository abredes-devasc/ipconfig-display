import requests

site = "https://ifconfig.co/ip"
response = requests.get(url=site)
print(f"HTTP: {response.status_code}")
print(f"IP: {response.text}")

site = "https://ifconfig.co/asn"
response = requests.get(url=site)
print(f"HTTP: {response.status_code}")
print(f"ASN: {response.text}")

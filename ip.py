import requests

site = "https://ifconfig.co/json"
response = requests.get(url=site)
dic = response.json()

ip = dic.get("ip")
asn = dic.get("asn")
asn_org = dic.get("asn_org")
latitude = dic.get("latitude")
longitude = dic.get("longitude")

print(f"HTTP: {response.status_code}")
print(f"IP: {ip}")
print(f"ASN: {asn}")
print(f"LAT: {latitude}")
print(f"LON: {longitude}")
print(f"ASN_ORG: {asn_org}")

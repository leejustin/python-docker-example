import requests

print("HELLO!")

x = requests.get('https://docs.python-requests.org/en/master/')
print(x.text)

print("ADIOS")

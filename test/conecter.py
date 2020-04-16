import socks5
from urllib.request import urlopen

socks5.set_default_proxy(socks5.SOCKS5, "localhost", 9150)
print("Checking...")
print(urlopen('http://icanhazip.com').read())
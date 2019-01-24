import os
import subprocess

x = '127.0.0.1'
#scan2target = ['nmap', '--script', 'ssl-enum-ciphers', '-p 443', x]
scan2target = str(['nmap', '--script', 'ssl-enum-ciphers', '-p 443', x])
print (scan2target)
os.system('nmap --script ssl-enum-ciphers -p 443 127.0.0.1')
#result = os.system(scan2target)
#!/usr/bin/env python3

# Script basique pour parser un log SSH brut

import re

logfile = 'auth.log'

# Ouvre et lit le fichier
with open(logfile, 'r') as file:
    lines = file.readlines()

failed_logins = {}

# Regex simple pour capter les tentatives échouées SSH
for line in lines:
    if 'Failed password' in line:
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        if ip:
            ip = ip[0]
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

# Affichage clair des résultats
print("Tentatives SSH échouées par IP:")
for ip, attempts in failed_logins.items():
    print(f"{ip} : {attempts} tentatives")

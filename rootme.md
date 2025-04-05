# Write-Up : RootMe – TryHackMe

## 🎯 Objectif
Exploiter une faille web pour obtenir un shell, puis escalader les privilèges et rooter la machine.

---

## 🛠️ Outils utilisés
- Nmap
- Burp Suite
- Python reverse shell
- LinPEAS
- sudo misconfig

---

## 🧪 Étapes

### 🔍 1. Scan réseau
```bash
nmap -sC -sV -oN rootme_scan.txt 10.10.XX.XX
```
→ Port 80 avec site web simple, + port 22 ouvert.

---

### 🌐 2. Analyse Web
Fouille avec Burp Suite → injection dans un champ vulnérable.

Upload d’un **reverse shell Python** :

```bash
python3 -c 'import socket,os,pty;s=socket.socket(...); ...'
```

---

### 🔐 3. Escalade de privilèges
Lancement de LinPEAS pour audit des droits.

Découverte d’une commande sudo exécutable sans mot de passe.  
Utilisation de cette commande pour **obtenir root**.

---

## ✅ Résultat
Shell root + flag `/root/root.txt`

---

## 🧠 Ce que j’ai appris
- Injection web pour obtenir un shell
- Escalade sudo sans mot de passe
- Utilisation d’outils d’automatisation comme LinPEAS

# Write-Up : Kenobi – TryHackMe

## 🎯 Objectif
Gagner l'accès à une machine Linux vulnérable, exploiter un partage Samba, puis élever les privilèges pour obtenir un shell root.

---

## 🛠️ Outils utilisés
- Nmap
- Enum4linux
- smbclient
- Searchsploit
- Exploit local Linux (path hijacking)

---

## 🧪 Étapes

### 🔍 1. Scan réseau
```bash
nmap -sC -sV -oN kenobi_scan.txt 10.10.XX.XX
```
→ Découverte d’un partage Samba actif sur le port 445.

### 📂 2. Enumération Samba
```bash
enum4linux -a 10.10.XX.XX
```
→ Partage "anonymous" accessible sans mot de passe.

### 📁 3. Accès à un partage sans auth
```bash
smbclient //10.10.XX.XX/anonymous
```
→ Téléchargement d’un fichier contenant un exploit local.

### 🔎 4. Escalade de privilèges locale
Recherche d’exploit kernel ou de manipulation de PATH.

→ Utilisation d’un exploit path hijacking (`/usr/bin/menu`) pour obtenir root.

---

## ✅ Résultat
Obtenu le shell root + flag `/root/root.txt`

---

## 🧠 Ce que j’ai appris
- Enumération de Samba et partages Windows
- Exploitation de chemins vulnérables dans des scripts suid
- Importance des permissions et de l’environnement PATH

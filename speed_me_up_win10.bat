@echo off
:: Ova skripta će ubrzati win 10 uređaje tako što će iz startupa i Windows servisa maknuti pokretanje aplikacija, pozadinskih procesa, zadatci iz Task Schedulera, ubrzanje vizualnih performansi, koji nisu potrebni.
 
:: Info
echo Skripta ce ubrzati win 10 uredaje tako sto ce iz startupa i Windows servisa maknuti pokretanje aplikacija, pozadinskih procesa, zadatke iz Task Schedulera, ubrzanje vizualnih performansi, koji nisu potrebni.
 
:: Services
:: Disable Windows Search Service
powershell -Command "Stop-Service -Name 'WSearch' -Force"
powershell -Command "Set-Service -Name 'WSearch' -StartupType Disabled"
 
:: Disable Xbox Accessories
powershell -Command "Stop-Service -Name 'XboxGipSvc' -Force"
powershell -Command "Set-Service -Name 'XboxGipSvc' -StartupType Disabled"
 
:: Disable SysMain
powershell -Command "Stop-Service -Name 'SysMain' -Force"
powershell -Command "Set-Service -Name 'SysMain' -StartupType Disabled"
 
:: Disable bthserv Bluetooth Support Service
powershell -Command "Stop-Service -Name 'bthserv' -Force"
powershell -Command "Set-Service -Name 'bthserv' -StartupType Disabled"
 
:: Disable BTAGService Bluetooth Audio Gateway Service
powershell -Command "Stop-Service -Name 'BTAGService' -Force"
powershell -Command "Set-Service -Name 'BTAGService' -StartupType Disabled"
 
:: Disable WbioSrvc Windows Biometric Service
powershell -Command "Stop-Service -Name 'WbioSrvc' -Force"
powershell -Command "Set-Service -Name 'WbioSrvc' -StartupType Disabled"
 
:: Disable Usluga Windows Insider
powershell -Command "Stop-Service -Name 'wisvc' -Force"
powershell -Command "Set-Service -Name 'wisvc' -StartupType Disabled"
 
:: Disable GameInput Service
powershell -Command "Stop-Service -Name 'GameInputSvc' -Force"
powershell -Command "Set-Service -Name 'GameInputSvc' -StartupType Disabled"
 
:: Disable Geolocation Service
powershell -Command "Stop-Service -Name 'lfsvc' -Force"
powershell -Command "Set-Service -Name 'lfsvc' -StartupType Disabled"
 
:: Disable Touch Keyboard and Handwriting Panel Service
powershell -Command "Stop-Service -Name 'TabletInputService' -Force"
powershell -Command "Set-Service -Name 'TabletInputService' -StartupType Disabled"
 
:: Disable Windows Connect Now – registrator Config
powershell -Command "Stop-Service -Name 'wcncsvc' -Force"
powershell -Command "Set-Service -Name 'wcncsvc' -StartupType Disabled"
 
:: Disable Wi-Fi Direct Services Connection Manager Service
powershell -Command "Stop-Service -Name 'WFDSConMgrSvc' -Force"
powershell -Command "Set-Service -Name 'WFDSConMgrSvc' -StartupType Disabled"
 
:: Disable Windows Error Reporting Service
powershell -Command "Stop-Service -Name 'WerSvc' -Force"
powershell -Command "Set-Service -Name 'WerSvc' -StartupType Disabled"
 
:: Disable Servis mobilne pristupne točke u sustavu Windows
powershell -Command "Stop-Service -Name 'icssvc' -Force"
powershell -Command "Set-Service -Name 'icssvc' -StartupType Disabled"
 
:: Disable Upravljanje provjerom autorizacije za Xbox Live
powershell -Command "Stop-Service -Name 'XblAuthManager' -Force"
powershell -Command "Set-Service -Name 'XblAuthManager' -StartupType Disabled"
 
:: Isključivanje pozadinskih aplikacija - settings - privacy - background apps
:: Disable Background Apps
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications' -Name 'GlobalUserDisabled' -Value 1"
 
:: Isključivanje vizualnih efekta - settings - system - about - advanced settings - performance - visual effects
:: Set Performance Options - Visual Effects to Best Performance
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects' -Name 'VisualFXSetting' -Value 2"
 
:: Isključivanje servisa iz Task Schedulera
:: Disable Adobe Acrobat Update Task in Task Scheduler
schtasks /Change /TN "\Adobe Acrobat Update Task" /Disable
 
:: Disable MicrosoftEdgeUpdateTaskMachineCore
schtasks /Change /TN "\MicrosoftEdgeUpdateTaskMachineCore" /Disable
 
:: Disable MicrosoftEdgeUpdateTaskMachineUA
schtasks /Change /TN "\MicrosoftEdgeUpdateTaskMachineUA" /Disable
 
:: Disable XblGameSaveTask
schtasks /Change /TN "Microsoft\XblGameSave\XblGameSaveTask" /Disable
 
:: Disable Bluetooth\UninstallDeviceTask
schtasks /Change /TN "Microsoft\Windows\Bluetooth\UninstallDeviceTask" /Disable
 
:: Disable OfficeTelemetryAgent
schtasks /Change /TN "\Microsoft\Office\OfficeTelemetryAgentLogOn" /Disable
schtasks /Change /TN "\Microsoft\Office\OfficeTelemetryAgentFallBack" /Disable
 
:: Disable Microsoft\Windows\CloudExperienceHost\UninstallDeviceTask
schtasks /Change /TN "Microsoft\Windows\CloudExperienceHost\CreateObjectTask" /Disable
 
:: Disable Microsoft\Windows\CloudRestore\Backup
schtasks /Change /TN "Microsoft\Windows\CloudRestore\Backup" /Disable
 
:: Disable Microsoft\Windows\Customer Experience Improvement Program\CloudRestore\Consolidator
schtasks /Change /TN "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /Disable
 
:: Disable Microsoft\Windows\Customer Experience Improvement Program\UsbCeip
schtasks /Change /TN "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /Disable
 
:: Disable \Microsoft\Windows\Feedback\Siuf\DmClient
schtasks /Change /TN "\Microsoft\Windows\Feedback\Siuf\DmClient" /Disable
 
:: Disable \Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload
schtasks /Change /TN "\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload" /Disable
 
:: Disable \Microsoft\Windows\Flighting\FeatureConfig\ReconcileFeatures
schtasks /Change /TN "\Microsoft\Windows\Flighting\FeatureConfig\ReconcileFeatures" /Disable
 
:: Disable \Microsoft\Windows\Flighting\FeatureConfig\UsageDataFlushing
schtasks /Change /TN "\Microsoft\Windows\Flighting\FeatureConfig\UsageDataFlushing" /Disable
 
:: Disable \Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting
schtasks /Change /TN "\Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting" /Disable
 
:: Disable \Microsoft\Windows\Flighting\OneSettings\RefreshCache
schtasks /Change /TN "\Microsoft\Windows\Flighting\OneSettings\RefreshCache" /Disable
 
:: Disable \Microsoft\Windows\Application Experience\MareBackup
schtasks /Change /TN "\Microsoft\Windows\Application Experience\MareBackup" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\PcaPatchDbTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\PcaWallpaperAppDetect" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\ProgramDataUpdater" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\StartupAppTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Autochk\Proxy" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Windows Error Reporting\QueueReporting" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Windows Media Sharing\UpdateLibrary" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\NlaSvc\WiFiTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Maps\MapsToastTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Maps\MapsUpdateTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\PushToInstall\LoginCheck" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\PushToInstall\Registration" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\HelloFace\FODCleanupTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Speech\SpeechModelDownloadTask" /Disable
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Mobile Broadband Accounts\MNO Metadata Parser" /Disable
 
:: Deleting Win temp folder and skip if cant delete
del /s /q "C:\Windows\Temp\*.*" && rmdir /s /q "C:\Path\To\Your\Folder"
 
:: Brisanje temp foldera od korisnika
setlocal enabledelayedexpansion
 
REM Set the directory containing the folder names
set "inputDir=C:\Users"
 
REM Loop through each directory name in the input directory
for /d %%D in ("%inputDir%\*") do (
	set "dirName=%%~nxD"
	echo Processing directory: !dirName!
	REM Delete files from the Temp directory for the current directory name
	del /s /q "C:\Users\!dirName!\AppData\Local\Temp\*.*"
	if exist "C:\Users\!dirName!\AppData\Local\Temp\" (
    	echo Could not delete some files in !dirName!
	) else (
    	echo Successfully deleted files in !dirName!
	)
)
endlocal
 
:: Disable DiagTrack Telemetry
echo Disabling DiagTrack Telemetry
powershell -Command "Set-Service DiagTrack -StartupType Disabled"
echo Done.
 
:: Disable GUI on startup
echo Disabling GUI on startup
cmd.exe /c "bcdedit /set quietboot on"
echo Done.
 
:: Disable WindowsAnimations
echo Disable WindowsAnimations
powershell -Command 'Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "WindowAnimations" -Value 0'
echo Done.
 
:: Disable Cortana
echo Disable Cortana
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f
echo Done.
 
:: Delete Prefetch folder
echo Delete Prefetch folder
del /q/f/s C:\Windows\Prefetch\*
echo Done.
 
:: Disable Work Folders
echo Disable Work Folders
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'WorkFolders-Client' -NoRestart"
echo Done.
 
:: Disable Microsoft PrintToPDF
echo Disable Microsoft PrintToPDF
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'Printing-PrintToPDFServices-Features' -NoRestart"
echo Done.
 
:: Disable Microsoft Print XPS
echo Disable Microsoft Print XPS
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'Printing-XPSServices-Features' -NoRestart"
echo Done.
 
:: Remove Default printers
echo Remove Default printers
powershell -Command "Remove-Printer -Name 'Pošalji u OneNote 16'"
powershell -Command "Remove-Printer -Name 'Fax'"
echo Done.
 
:: Disable Activity History
echo Disable Activity History
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v PublishUserActivities /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v UploadUserActivities /t REG_DWORD /d 0 /f
echo Done.
 
:: Disable Diagnostics & Feedback
echo Disable Diagnostics Feedback
reg add "HKCU\Software\Microsoft\Siuf\Rules" /v NumberOfSIUFInPeriod /t REG_DWORD /d 0 /f
reg add "HKCU\Software\Microsoft\Siuf\Rules" /v PeriodInNanoSeconds /t REG_QWORD /d 0 /f
echo Done.
 
:: Disable GUI Transparency
echo Disable GUI Transparency
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize' -Name 'EnableTransparency' -Value 0"
echo Done.
 
:: Bluetooth service
echo Disabling some Bluetooth service.
powershell -Command "Set-Service -Name "BthAvctpSvc" -StartupType Disabled"
echo Done.
 
:: Wifi service
echo Disabling some Wifi service.
powershell -Command "Set-Service -Name "Wcmsvc" -StartupType Disabled"
echo Done.
 
:: Disable WavesSysSvc audio
echo Disabling WavesSysSvc audio
powershell -Command "Set-Service -Name "WavesSysSvc" -StartupType Disabled"
echo Done.
 
:: Disable WavesAudioService audio
echo Disabling WavesAudioService audio
powershell -Command "Set-Service -Name "WavesAudioService" -StartupType Disabled"
echo Done.
 
:: Remove Microsoft.XboxGamingOverlay
echo Remove Microsoft.XboxGamingOverlay and Gamebar
reg add "HKCU\Software\Microsoft\GameBar" /v AutoGameModeEnabled /t REG_DWORD /d 0 /f
reg add "HKCU\Software\Microsoft\GameBar" /v ShowStartupOverlay /t REG_DWORD /d 0 /f
:: Set-ItemProperty -Path "HKCU:\Software\Microsoft\GameBar" -Name "AutoGameModeEnabled" -Value 0
:: Set-ItemProperty -Path "HKCU:\Software\Microsoft\GameBar" -Name "ShowStartupOverlay" -Value 0
:: Get-AppxPackage -AllUsers *Microsoft.XboxGamingOverlay* | Remove-AppxPackage
:: Get-AppxPackage *Microsoft.XboxGamingOverlay* | Remove-AppxPackage
echo Done.
 
:: Disable and uninstall Onedrive
echo Uninstall OneDrive
taskkill /f /im OneDrive.exe
%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall
echo Done.
 
:: Run sfc /scannow scans and repairs corrupted or missing system files
echo sfc /scannow komanda skenira i popravlja korumpirane sistemske dokumente koji fale. Ako je presporo možete ugasiti prozor, ostalo je sve napravljeno.
sfc /scannow
 
:: Final message
echo Skripta je zavrsila sa radom.
echo "*************************"
echo "* Restartajte racunalo. *"
echo "*************************"
 
pause


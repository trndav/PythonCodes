@echo off
:: The script will speed up win 10 devices by removing the startup of some applications (OneDrive), background processes and services (like Location, Mobile, Maps, Xbox), delete temp files, disable some Task Scheduler tasks, acceleration of visual performance and some other minor details. Run this .bat file from computer and script will do the rest.
 
:: Info
echo The script will speed up win 10 devices by removing the startup of some applications (OneDrive), background processes and services (like Location, Mobile, Maps, Xbox), delete temp files, disable some Task Scheduler tasks, acceleration of visual performance and some other minor details. Run this .bat file from computer and script will do the rest.
 
:: Services
 
:: Disable Windows Search Service
echo Disable wsearch
powershell -Command "Stop-Service -Name 'WSearch' -Force"
powershell -Command "Set-Service -Name 'WSearch' -StartupType Disabled"
echo Task done.
 
:: Disable Xbox Accessories
echo Disable XboxGipSvc
powershell -Command "Stop-Service -Name 'XboxGipSvc' -Force"
powershell -Command "Set-Service -Name 'XboxGipSvc' -StartupType Disabled"
echo Task done.
 
:: Disable SysMain
echo Disable Sysmain
powershell -Command "Stop-Service -Name 'SysMain' -Force"
powershell -Command "Set-Service -Name 'SysMain' -StartupType Disabled"
echo Task done.
 
:: Disable bthserv Bluetooth Support Service
echo Disable bthserv Bluetooth Support Service
powershell -Command "Stop-Service -Name 'bthserv' -Force"
powershell -Command "Set-Service -Name 'bthserv' -StartupType Disabled"
echo Task done.
 
:: Disable BTAGService Bluetooth Audio Gateway Service
echo Disable BTAGService Bluetooth Audio Gateway Service
powershell -Command "Stop-Service -Name 'BTAGService' -Force"
powershell -Command "Set-Service -Name 'BTAGService' -StartupType Disabled"
echo Task done.
 
:: Disable WbioSrvc Windows Biometric Service
echo Disable WbioSrvc Windows Biometric Service
powershell -Command "Stop-Service -Name 'WbioSrvc' -Force"
powershell -Command "Set-Service -Name 'WbioSrvc' -StartupType Disabled"
echo Task done.
 
:: Disable Usluga Windows Insider
echo Disable Usluga Windows Insider
powershell -Command "Stop-Service -Name 'wisvc' -Force"
powershell -Command "Set-Service -Name 'wisvc' -StartupType Disabled"
echo Task done.
 
:: Disable GameInput Service
echo Disable GameInput Service
powershell -Command "Stop-Service -Name 'GameInputSvc' -Force"
powershell -Command "Set-Service -Name 'GameInputSvc' -StartupType Disabled"
echo Task done.
 
:: Disable Geolocation Service
echo Disable Geolocation Service
powershell -Command "Stop-Service -Name 'lfsvc' -Force"
powershell -Command "Set-Service -Name 'lfsvc' -StartupType Disabled"
echo Task done.
 
:: Disable Touch Keyboard and Handwriting Panel Service
echo Disable Touch Keyboard and Handwriting Panel Service
powershell -Command "Stop-Service -Name 'TabletInputService' -Force"
powershell -Command "Set-Service -Name 'TabletInputService' -StartupType Disabled"
echo Task done.
 
:: Disable Windows Connect Now – registrator Config
echo Disable Windows Connect Now – registrator Config
powershell -Command "Stop-Service -Name 'wcncsvc' -Force"
powershell -Command "Set-Service -Name 'wcncsvc' -StartupType Disabled"
echo Task done.
 
:: Disable Wi-Fi Direct Services Connection Manager Service
echo Disable Wi-Fi Direct Services Connection Manager Service
powershell -Command "Stop-Service -Name 'WFDSConMgrSvc' -Force"
powershell -Command "Set-Service -Name 'WFDSConMgrSvc' -StartupType Disabled"
echo Task done.
 
:: Disable Windows Error Reporting Service
echo Disable Windows Error Reporting Service
powershell -Command "Stop-Service -Name 'WerSvc' -Force"
powershell -Command "Set-Service -Name 'WerSvc' -StartupType Disabled"
echo Task done.
 
:: Disable Servis mobilne pristupne točke u sustavu Windows
echo Disable Servis mobilne pristupne točke u sustavu Windows
powershell -Command "Stop-Service -Name 'icssvc' -Force"
powershell -Command "Set-Service -Name 'icssvc' -StartupType Disabled"
echo Task done.
 
:: Disable Upravljanje provjerom autorizacije za Xbox Live
echo Disable Upravljanje provjerom autorizacije za Xbox Live
powershell -Command "Stop-Service -Name 'XblAuthManager' -Force"
powershell -Command "Set-Service -Name 'XblAuthManager' -StartupType Disabled"
echo Task done.
 
:: Disable Adobe ************
echo Disable Adobe
powershell -Command "Stop-Service -Name 'AdobeARMservice' -Force"
powershell -Command "Set-Service -Name 'AdobeARMservice' -StartupType Disabled"
echo Task done.
 
:: Isključivanje pozadinskih aplikacija - settings - privacy - background apps
echo Disable Background Apps
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications' -Name 'GlobalUserDisabled' -Value 1"
echo Task done.
 
:: Isključivanje vizualnih efekta - settings - system - about - advanced settings - performance - visual effects
echo Disable Visual Effects to Best Performance
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects' -Name 'VisualFXSetting' -Value 2"
echo Task done.
 
:: Isključivanje servisa iz Task Schedulera
echo Disable Adobe Acrobat Update Task in Task Scheduler
schtasks /Change /TN "\Adobe Acrobat Update Task" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Location in Task Scheduler ***
echo Disable \Microsoft\Windows\Location in Task Scheduler
schtasks /Change /TN "\Microsoft\Windows\Location\Notifications" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Location\WindowsActionDialog in Task Scheduler ***
echo Disable \Microsoft\Windows\Location\WindowsActionDialog in Task Scheduler
schtasks /Change /TN "\Microsoft\Windows\Location\WindowsActionDialog" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\MobilePC in Task Scheduler ***
schtasks /Change /TN "\Microsoft\Windows\MobilePC\HotStart" /Disable
echo Task done.
 
:: Disable MicrosoftEdgeUpdateTaskMachineCore
schtasks /Change /TN "\MicrosoftEdgeUpdateTaskMachineCore" /Disable
echo Task done.
 
:: Disable MicrosoftEdgeUpdateTaskMachineUA
schtasks /Change /TN "\MicrosoftEdgeUpdateTaskMachineUA" /Disable
echo Task done.
 
:: Disable XblGameSaveTask
schtasks /Change /TN "Microsoft\XblGameSave\XblGameSaveTask" /Disable
echo Task done.
 
:: Disable Bluetooth\UninstallDeviceTask
schtasks /Change /TN "Microsoft\Windows\Bluetooth\UninstallDeviceTask" /Disable
echo Task done.
 
:: Disable Microsoft\Windows\CloudExperienceHost\UninstallDeviceTask
schtasks /Change /TN "Microsoft\Windows\CloudExperienceHost\CreateObjectTask" /Disable
echo Task done.
 
:: Disable Microsoft\Windows\CloudRestore\Backup
schtasks /Change /TN "Microsoft\Windows\CloudRestore\Backup" /Disable
echo Task done.
 
:: Disable Microsoft\Windows\Customer Experience Improvement Program\CloudRestore\Consolidator
schtasks /Change /TN "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /Disable
echo Task done.
 
:: Disable Microsoft\Windows\Customer Experience Improvement Program\UsbCeip
schtasks /Change /TN "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Feedback\Siuf\DmClient
schtasks /Change /TN "\Microsoft\Windows\Feedback\Siuf\DmClient" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload
schtasks /Change /TN "\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Flighting\FeatureConfig\ReconcileFeatures
schtasks /Change /TN "\Microsoft\Windows\Flighting\FeatureConfig\ReconcileFeatures" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Flighting\FeatureConfig\UsageDataFlushing
schtasks /Change /TN "\Microsoft\Windows\Flighting\FeatureConfig\UsageDataFlushing" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting
schtasks /Change /TN "\Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Flighting\OneSettings\RefreshCache
schtasks /Change /TN "\Microsoft\Windows\Flighting\OneSettings\RefreshCache" /Disable
echo Task done.
 
:: Disable \Microsoft\Windows\Application Experience\MareBackup
schtasks /Change /TN "\Microsoft\Windows\Application Experience\MareBackup" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\PcaPatchDbTask" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\PcaWallpaperAppDetect" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\ProgramDataUpdater" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Application Experience\StartupAppTask" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Autochk\Proxy" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Windows Error Reporting\QueueReporting" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Windows Media Sharing\UpdateLibrary" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\NlaSvc\WiFiTask" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Maps\MapsToastTask" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\Maps\MapsUpdateTask" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\PushToInstall\LoginCheck" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\PushToInstall\Registration" /Disable
echo Task done.
 
:: Disable
schtasks /Change /TN "\Microsoft\Windows\HelloFace\FODCleanupTask" /Disable
echo Task done.
 
:: Disable
echo Disable SpeechModelDownloadTask
schtasks /Change /TN "\Microsoft\Windows\Speech\SpeechModelDownloadTask" /Disable
echo Task done.
 
:: Disable MNO Metadata Parser
echo Disable MNO Metadata Parser
schtasks /Change /TN "\Microsoft\Windows\Mobile Broadband Accounts\MNO Metadata Parser" /Disable
echo Task done.
 
:: Disable OfficeTelemetryAgent
echo Disable OfficeTelemetryAgent
schtasks /Change /TN "\Microsoft\Office\OfficeTelemetryAgentLogOn" /Disable
schtasks /Change /TN "\Microsoft\Office\OfficeTelemetryAgentFallBack" /Disable
echo Task done.
 
:: Disable Windows Compatibility Telemetry Task
echo Disable Windows Compatibility Telemetry Task
schtasks /Change /TN "Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /Disable
echo Task done.
 
:: Deleting Win temp folder and skip if cant delete
echo Delete Win temp folder
del /s /q "C:\Windows\Temp\*.*"
echo Task done.
 
:: Brisanje temp foldera od svih korisnika
echo Deleting local user temp directories from users directory
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
echo Task done.
 
:: Disable GUI on startup
echo Disabling GUI on startup
cmd.exe /c "bcdedit /set quietboot on"
echo Task done.
 
:: Disable WavesSysSvc audio
echo Disabling WavesSysSvc audio
powershell -Command "Set-Service -Name "WavesSysSvc" -StartupType Disabled"
echo Task done.
 
:: Disable WavesAudioService audio
echo Disabling WavesAudioService audio
powershell -Command "Set-Service -Name "WavesAudioService" -StartupType Disabled"
echo Task done.
 
:: Disable GUI Transparency
echo Disable GUI Transparency
powershell -Command "Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize' -Name 'EnableTransparency' -Value 0"
echo Task done.
 
:: Disable WindowsAnimations
echo Disable WindowsAnimations
powershell -Command 'Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "WindowAnimations" -Value 0'
echo Task done.
 
:: Disable DiagTrack Telemetry
echo Disabling DiagTrack Telemetry
powershell -Command "Set-Service DiagTrack -StartupType Disabled"
echo Task done.
 
:: Disable GUI on startup
echo Disabling GUI on startup
cmd.exe /c "bcdedit /set quietboot on"
echo Task done.
 
:: Disable Work Folders
echo Disable Work Folders
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'WorkFolders-Client' -NoRestart"
echo Task done.
 
:: Bluetooth service
echo Disabling some Bluetooth service.
powershell -Command "Set-Service -Name "BthAvctpSvc" -StartupType Disabled"
echo Task done.
 
:: Disable Microsoft PrintToPDF
echo Disable Microsoft PrintToPDF
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'Printing-PrintToPDFServices-Features' -NoRestart"
echo Task done.
 
:: Disable Microsoft Print XPS
echo Disable Microsoft Print XPS
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'Printing-XPSServices-Features' -NoRestart"
echo Task done.
 
:: Disable Fax Services
powershell -Command "Disable-WindowsOptionalFeature -Online -FeatureName 'FaxServicesClientPackage' -NoRestart"
echo Task done.
 
:: Disable Cortana
echo Disable Cortana
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f
echo Task done.
 
:: Disable Windows Tips and Notifications
echo Disable Windows Tips and Notifications
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SubscribedContent-338388Enabled /t REG_DWORD /d 0 /f
echo Task done.
 
:: Disable Onedrive sync
echo Disable Onedrive sync
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\SyncSettings" /v Enabled /t REG_DWORD /d 0 /f
echo Task done.
 
:: Useful on touchscreen devices or tablets
echo Disable PenWorkspace useful on touchscreen devices or tablets
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PenWorkspace" /v PenWorkspaceEnabled /t REG_DWORD /d 0 /f
echo Task done.
 
:: Disabled Suggested apps and Welcome experience, Microsoft tips
echo Disabled Suggested apps and Welcome experience, Microsoft tips
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SubscribedContent-310093Enabled /t REG_DWORD /d 0 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" /v SubscribedContent-338389Enabled /t REG_DWORD /d 0 /f
echo Task done.
 
:: Disable Windows Store Auto Updates
echo Disable Windows Store Auto Updates
reg add "HKLM\SOFTWARE\Policies\Microsoft\WindowsStore" /v AutoDownload /t REG_DWORD /d 2 /f
echo Task done.
 
:: Disable Windows Spotlight on Lock Screen
echo Disable Windows Spotlight on Lock Screen
reg add "HKCU\Software\Policies\Microsoft\Windows\CloudContent" /v DisableWindowsSpotlightFeatures /t REG_DWORD /d 1 /f
echo Task done.
 
:: Disable Windows Media Player Network Sharing Service
echo Disable Windows Media Player Network Sharing Service
powershell -Command Set-Service -Name "WMPNetworkSvc" -StartupType Disabled
echo Task done.
 
:: Disable Windows Perception Simulation Service
echo Disable Windows Perception Simulation Service
powershell -Command Set-Service -Name "PerceptionSimulation" -StartupType Disabled
echo Task done.
 
:: Disable Windows Help and Support Service
echo Disable Windows Help and Support Service
powershell -Command Set-Service -Name "helpsvc" -StartupType Disabled
echo Task done.
 
:: Disable and uninstall Onedrive
echo Uninstall OneDrive
taskkill /f /im OneDrive.exe
%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall
echo Task done.
 
:: Run sfc /scannow scans and repairs corrupted or missing system files
echo sfc /scannow komanda skenira i popravlja korumpirane sistemske dokumente koji fale. Ako je presporo možete ugasiti prozor, ostalo je sve napravljeno.
sfc /scannow
echo Task done.
 
:: Final message
echo Skripta je zavrsila sa radom.
echo Restartajte racunalo.
 
pause

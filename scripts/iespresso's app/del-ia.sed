[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=0
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=6144
RebootMode=N
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles
[Strings]
InstallPrompt=Do you want to clone and install Del-ia?
DisplayLicense=
FinishMessage=
TargetName=C:\Users\Guillermo\Desktop\prueba.EXE
FriendlyName=Del-ia's Cloner Repository & Installer
AppLaunched=cmd /c iespress.bat
PostInstallCmd=<None>
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="clean.bat"
FILE1="iespress.bat"
FILE2="iespress.vbs"
FILE3="post.bat"
[SourceFiles]
SourceFiles0=C:\Users\Guillermo\Desktop\Scripting\
[SourceFiles0]
%FILE0%=
%FILE1%=
%FILE2%=
%FILE3%=

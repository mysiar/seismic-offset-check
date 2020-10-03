@echo off
for /f %%i in ('git describe --tags') do set GIT_TAG=%%i

rmdir dist /s /q
rmdir build /s /q

pyinstaller main.py -n OffsetCheck --windowed
xcopy icons dist\OffsetCheck\icons\
cd dist
powershell Compress-Archive OffsetCheck ../dist-out/OffsetCheck-%GIT_TAG%.win.zip
cd ..
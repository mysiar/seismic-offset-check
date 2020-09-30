rmdir dist /s /q
rmdir build /s /q

pyinstaller main.py -n OffsetCheck --windowed
xcopy icons dist\OffsetCheck\icons\
cd dist
powershell Compress-Archive OffsetCheck ../dist-out/OffsetCheck-win.zip
cd ..
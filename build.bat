rmdir dist /s /q
rmdir build /s /q

pyinstaller main.py -n OffsetCheck --windowed
xcopy icons dist\OffsetCheck\icons\
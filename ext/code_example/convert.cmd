set HOME=%~dp0
set NAME=%~n1
set OUT_DIR=%~dp2
"%HOME%\colorer\colorer.exe" -c "%HOME%\colorer\base\catalog.xml" -h "%1" -dc -i htmlcss >"%TEMP%\%NAME%.html" 2>"%HOME%\convert.log"
mkdir "%OUT_DIR%"
copy "%HOME%\hrdstyle.css" "%TEMP%"
"%HOME%\ieCapt.exe" --min-width=640 --url="file:///%TEMP%\%NAME%.html" --out="%2" >>"%HOME%\convert.log" 2>>&1
del "%TEMP%\%NAME%.html"
del "%TEMP%\hrdstyle.css"

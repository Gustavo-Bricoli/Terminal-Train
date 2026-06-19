@echo off

echo Limpando arquivos antigos...

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist main.spec del /f /q main.spec

echo.
echo Gerando executavel...

py -m PyInstaller --onedir ^
--add-data "Sons;Sons" ^
--add-data "Animacoes;Animacoes" ^
main.py

echo.
echo Processo concluido!
echo Executavel em:
echo dist\main\main.exe

pause
@echo off
:inicio
cls
python main.py %*

echo Bot detenido. �Desea volver a ejecutarlo? (S/N)
choice /c SN /m "Presione S para volver a ejecutar o N para salir: "
if errorlevel 2 (
        exit /b 1
) else (
        goto inicio
 )

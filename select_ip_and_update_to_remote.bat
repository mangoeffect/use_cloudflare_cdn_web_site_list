:: auto update host file
@echo off
setlocal enabledelayedexpansion

git checkout shenzhen1

:: select the best ip for cloudflare
echo.|CloudflareST.exe

SET /a n = 0
for /f "tokens=1 delims=," %%i in (result.csv) do (
    SET /a n+=1 
    If !n! equ 2 SET bestip=%%i
)

if "%bestip%"=="" (
    echo "ip is none"
    exit
) 

echo the best ip = %bestip%

python update_host.py --ip=%bestip% --domain=use_cloudflare_domain_list.txt

:: push update to remote
git add .

git commit -m "update best ip"

git pull

git push



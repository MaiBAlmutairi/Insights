@echo off


call yarn -v 2> Nul

if "%errorlevel%" == "9009" (
	call npm install
) else (
	call yarn install
)


SET env=%1
IF "%env%" == "" SET env=development

git branch | find "* master" > NUL & IF ERRORLEVEL 1 (
    ECHO Not master branch
) ELSE (
    SET env=production
)


echo "%env%" > "CURRENT_ENV"

ionic build --configuration=%env%
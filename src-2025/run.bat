@echo off
echo Running...
setlocal enabledelayedexpansion

:: NTS: Edit this so miniconda is installed automatically

call C:/Users/%USERNAME%/miniconda3/Scripts/activate.bat
if errorlevel 1 (
    call C:/Users/%USERNAME%/Anaconda3/Scripts/activate.bat    
    if errorlevel 1 (
        echo Cannot use conda from the current command prompt.
        echo Use the Anaconda Prompt or add your conda installation to PATH.
        pause
        exit /b 1
    )
)

:: echo Errorlevel after conda --version: %errorlevel%
call conda --version
if errorlevel 1 (
    echo Conda is not installed. Please install Miniconda first at
    echo https://www.anaconda.com/download/success.
    pause
    exit /b 1
) else (
    echo Conda detected.
)

:: echo Checking for Conda environment...
call conda env list > temp_env_list.txt
findstr "yt_archiver" temp_env_list.txt >nul

if errorlevel 1 (
    del temp_env_list.txt
    goto setup_conda_env
) else (
    del temp_env_list.txt
    goto activate_conda_env
)

:setup_conda_env

echo Setting up Conda environment...
call conda env create -f environment.yml

if errorlevel 1 (
    echo Failed to create conda environment. Check your environment.yml file.
    pause
    exit /b 1
)

echo Environment setup complete.

:activate_conda_env

echo Activating environment...

call conda activate yt_archiver
if errorlevel 1 (
    echo Failed to activate environment. Ensure Conda is properly set up in your shell.
    pause
    exit /b 1
)

cd contenter-v1/src-2025
call python main.py
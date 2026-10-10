@echo off
chcp 65001 > nul
title Knowledge Lab - Pipeline Manager
cd /d "%~dp0"
python 03_scripts\knowledge_cli.py
pause

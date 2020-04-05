@echo off
title Delia's Installing Dependencies

:: choco install -y python
:: choco install -y nodejs
npm install
py -3 -m venv venv

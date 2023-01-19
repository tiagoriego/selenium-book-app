# Selenium BOOK APP

## Initial

```bash
git clone https://github.com/tiagoriego/book-api
```

## Requirements

Python Version `3.10.5` and Pyenv Version `2.3.9`

```bash
pyenv virtualenv 3.10.5 selenium-book-app
echo selenium-book-app > ./selenium-book-app/.python-version
cd selenium-book-app
```

### Install Packages

```bash
pip install -r requirements.txt
```

## Drivers

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

* [About Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)
* [Drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)
  
I'm using [chromium drive](https://sites.google.com/chromium.org/driver/?pli=1)

For Linux:

[Download Here](https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.71/)

### Bash

Make dir `~/projects/selenium/driver`

```bash
cd ~/projects/selenium/driver
cp ~/Download/chromedriver_linux64.zip .
unzip chromedriver_linux64.zip 
rm chromedriver_linux64.zip
```

```bash
echo 'export PATH="$HOME/projects/selenium/driver:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

### Execute command

```bash
chromedriver
```

Output

```bash
Starting ChromeDriver 108.0.5359.71 (1e0e3868ee06e91ad636a874420e3ca3ae3756ac-refs/branch-heads/5359@{#1016}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```

`CTRL+C` to scape

I'm using version `ChromeDriver 108.0.5359.71` becouse of my version local

### Set Hard Coded Location

```python
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/projects/selenium/driver/chromedriver")
driver = webdriver.Chrome(service=service)
```

## AUTOPEP8 VSCODE

Formatting code `CTRL+Shift+i`


## Start

First you need to run other services:

[Book API](https://github.com/tiagoriego/book-api)

```bash
cd ./book-api/src/app
uvicorn main:app --port 8080
```

[Book App](https://github.com/tiagoriego/book-app)

```bash
cd ./book-app
npm start
```

And finally

`.env`

```bash
cp .env.example .env
source ./.env
```

Execute

```bash
python app.py
```

## Selenium

[Doc](https://selenium-python.readthedocs.io/installation.html#)
# ExchangeRates
Exchange Rates Tracking Tool Asynchronous App created in Python with Selenium, TinyDB and FastAPI.

## Table of contents
* [General info](#gen-info)
* [Technologies](#tech)
* [Setup](#setup)
* [Usage](#use)

## General info
This project is VPS friendly structure of lightweight database and web-scrapper. 
It may be used to periodically grab (with crone) and store exchange rates data.
Requests to server are handled by json responses according to requests.

## Technologies
Project is created with:
* Python == 3.6.8
* fastapi == 0.63.0
* selenium == 3.141.0
* starlette == 0.13.6
* tinydb == 4.3.0
* uvicorn == 0.13.2
* and many more, required packages are listed in requirements.txt file.

## Setup
To run this project, please install all dependencies listed in requirements.txt.
```
$ pip install -r requirements.txt 
```
Configure local host and port in main.py file to meet your needs:
```
uvicorn.run(app, host="127.0.0.1", port=8000)
```
Run this project with either:
* crone_script.py
it runs project in database + scrapper mode. It updates database records and does not run API.

* main.py
Runs crone_script.py with FastAPI.

Valid currencies are configured by Currencies class in models.py, it may be extended to any currency that is "Google'd" friendly.

## Usage
Docs for the App can be found at host/docs.
List of valid requests:
```
* today/{currency}
```
Responses with todays records in format:
```
0:{
'date': string
'hour': string
'value: float
}
```
etc.
```
* all/{currency}
```
Responses with all records stored in db for requested currency.
```
* dates/{currency}/?q=start&q=end  
```
query example: 
```
dates/usd/?q=01-12-2020&q=29-12-2020
```







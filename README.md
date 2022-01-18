# top.gg autovoter

Python program that utilizes the selenium library to vote for bots on top.gg.

## Description

The program opens a top.gg vote site, given a bot ID. It then logs in using the discord tokens provided and votes for the bot. Works with multiple tokens, though there is a cap per IP (refer to additional information below).

## Requirements

- Chromedriver
- Python 3
- Selenium
- Discord tokens

## Installation

- Clone repo
- Run ```pip install -r requirements.txt```
- Download chromedriver and add to PATH
- Rename tokens.txt.example to tokens.txt and fill in discord tokens
- Edit config variables at the start of ```multivote.py```
- Run ```multivote.py```

## Additional information

- There is a cap to how many times you can vote from a certain IP, support for scraping proxies is currently not available.

## Acknowledgements

- [add_token function](https://github.com/RealMoondancer/DiscordTokenLogin/blob/main/main.py)

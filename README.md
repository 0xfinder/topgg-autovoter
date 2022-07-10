# top.gg autovoter

Python program that utilizes the selenium library to vote for bots on top.gg.

## Description

The program opens a top.gg vote site, given a bot ID. It then logs in using the discord tokens provided and votes for the bot. Works with multiple tokens, though there is a cap per IP (refer to additional information below).

## Requirements

- Chrome beta version (As of 10 Jul 2022, latest chrome version 103 does NOT work, install chrome beta v104 [here](https://www.google.com/chrome/beta/))
- Chromedriver (Included binary in this repo [here](chromedriver.exe) so i doubt you have to install)
- Python 3
- Selenium
- Discord tokens

## Installation

- Clone repo
- `cd` into the directory
- Run `pip install -r requirements.txt`
- ~~Download chromedriver and add to PATH~~
- Rename tokens.txt.example to tokens.txt and fill in discord tokens
- Edit config variables in `config.json`
- Run `multivote.py`

## Help

- `multivote.py -h`

## Examples

- Running with arguments

```
# Votes for bot with id
python multivote.py -b 432610292342587392
```

## Additional information

- There is a cap to how many times you can vote from a certain IP, support for scraping proxies is currently not available.

## Acknowledgements

- [add_token function](https://github.com/RealMoondancer/DiscordTokenLogin/blob/main/main.py)

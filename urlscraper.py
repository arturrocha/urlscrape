#!/usr/bin/python3
import time
import random
from datetime import date, datetime, timedelta
from scrape import get_url
#from telegram_bot import send_message

def scraper(website):
    url_list = get_url(website)
    return(url_list)
    
website = 'https://redeglobo.globo.com/'
res = scraper(website)
print(list(set(res)))
print(len(list(set(res))))
#for site in res:
#    print(scraper(site))
exit()

from bs4 import BeautifulSoup
import urllib.request
import requests
import time


class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'


def get_url(website):
    try:
        opener = AppURLopener()
        response = opener.open(website)
        soup = BeautifulSoup(response, "html.parser")
        result = html_parser(website, soup)
        return result
    except Exception as e:
        print(website)
        print(' |get news "scrape.py"| ', e)
        #debug(e, telegram_chat_id_admin)
        return False


def html_parser(website, soup):
    try:
        news_list = url_all(website, soup)
    except Exception as e:
        print('url_all error "scrape.py"', e)

    try:
        return news_list
    except Exception as e:
        print('news_parser_error "scrape.py"', e)
        return


def clear_blob(blob):
    blob_list = []
    blob = [var for var in blob]
    for var in blob:
        if 'http' in var:
            url = var.split('"')
            for blob2 in url:
                if 'http' in blob2 and blob2[-4:].lower() != '.gif' and blob2[-4:].lower() != '.jpg' and blob2[-5:].lower() != '.jpeg' and blob2[-6:].lower() != '.woff2'  and blob2[-4:].lower() != '.ico' and blob2[-4:].lower() != '.ttf' and blob2[-4:].lower() != '.pdf' and blob2[-5:].lower() != '.woff' and blob2[-4:].lower() != '.css'  and blob2[-4:].lower() != '.png':
                    blob2 = blob2.replace('</p>,', '')
                    blob2 = blob2.replace('url(\'', '')
                    blob2 = blob2.replace('url(', '')
                    blob2 = blob2.replace('\');', '')
                    blob2 = blob2.replace(' ', '')
                    blob2 = blob2.replace(');', '')
                    blob2 = blob2.replace('\';', '')
                    blob2 = blob2.replace('\'', '')
                    blob2 = blob2.replace('src=', '')
                    blob2 = blob2.replace('getCombine:', '')
                    blob2 = blob2.replace('},', '')
                    blob2 = blob2.replace('<div', '')
                    blob2 = blob2.replace('.</p>', '')
                    blob2 = blob2.replace('</p>', '')
                    blob2 = blob2.replace('<h4', '')
                    blob2 = blob2.replace('</a>', '')
                    blob2 = blob2.replace('<', '')
                    blob2 = blob2.replace('>', '')
                    blob2 = blob2.replace('(', '')
                    blob2 = blob2.replace(')', '')
                    blob2 = blob2.replace(',', '')
                    blob2 = blob2.replace('Janeiro&amp;display=popup&amp;href=', '')
                    blob2 = blob2.replace('Janeiro&amp;url=', '')
                    blob2 = blob2.replace('Janeiro&amp;body=', '')
                    blob2 = blob2.replace('Senate&amp;display=popup&amp;href=', '')
                    blob2 = blob2.replace('Senate&amp;body=', '')
                    blob2 = blob2.replace('MESS&amp;body=', '')
                    blob2 = blob2.replace('AVALANCHES&amp;body=', '')
                    blob2 = blob2.replace('POOR&amp;body=', '')
                    blob2 = blob2.replace('MOON&amp;body=', '')
                    blob2 = blob2.replace('2020&amp;body=', '')
                    blob2 = blob2.replace('BLAST&amp;body=', '')
                    blob2 = blob2.replace('DETAINED&amp;body=', '')
                    blob2 = blob2.replace('RUSSIA&amp;body=', '')
                    blob2 = blob2.replace('CHANGE&amp;body=', '')
                    blob2 = blob2.replace('32&amp;body=', '')
                    blob2 = blob2.replace('//polyfill', '')
                    blob2 = blob2.replace('}}.html&url=http://{{', '')
                    blob2 = blob2.replace('https://twitter.com/intent/tweet?text={{title}}&url=http://{{', '')
                    blob2 = blob2.replace('/script/div', '')
                    blob2 = blob2.replace('DMT.Utilities.openWindow', '')
                    blob2 = blob2.replace('DMT.SendToAFriend.media', '')
                    blob2 = blob2.replace('DMT.SendToAFriend.media', '')
                    blob2 = blob2.replace('javascript:POPUP.OPEN', '')
                    blob2 = blob2.replace('&quot;', '')
                    blob2 = blob2.replace('window.openhttp://twitter.com/siemens_pressreturn', '')

                    # after cleaning
                    print('blob', blob2)
                    #time.sleep(0.1)
                    blob_list.append(blob2)
    return blob_list


def url_all(website, soup):
    url_list = list(set(str(soup.find_all()).split(' ')))
    url_list = clear_blob(url_list)
    #print(url_list)
    # what we want
    #for url in new_url_list:
    #    news.append(url)
    return list(set(url_list))



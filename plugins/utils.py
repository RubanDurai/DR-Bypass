import re
import json
from configs import *
import aiohttp
import asyncio
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
from bs4 import BeautifulSoup
from urllib.parse import urlparse

async def main_convertor_handler(message:Message):
    caption = None

    if message.text:
        caption = message.text.html
    elif message.caption:
        caption = message.caption.html

    # caption = caption.replace("--", "")

    # Checking if the message has any link or not. If it doesn't have any link, it will return.
    if len(await extract_link(caption)) <=0 and not message.reply_markup:
        return

    # Getting the function for the user's method
    method_func = replace_link

    # converting urls
    shortenedText = await method_func(caption)

    # converting reply_markup urls
    reply_markup = await reply_markup_handler(message, method_func)


    if message.text:
        return await message.reply(shortenedText, disable_web_page_preview=True, reply_markup=reply_markup, quote=True, parse_mode=ParseMode.HTML)

    elif message.media:

        if message.document:
            return await message.reply_document(message.document.file_id, caption=shortenedText, reply_markup=reply_markup, quote=True, parse_mode=ParseMode.HTML)

        elif message.photo:
            return await message.reply_photo(message.photo.file_id, caption=shortenedText, reply_markup=reply_markup, quote=True, parse_mode=ParseMode.HTML)
  
# Reply markup 
async def reply_markup_handler(message:Message, method_func):
    if message.reply_markup:
        reply_markup = json.loads(str(message.reply_markup))
        buttsons = []
        for markup in reply_markup["inline_keyboard"]:
            buttons = []
            for j in markup:
                text = j["text"]
                url = j["url"]
                url = await method_func(url)
                button = InlineKeyboardButton(text, url=url)
                buttons.append(button)
            buttsons.append(buttons)
        reply_markup = InlineKeyboardMarkup(buttsons)
        return reply_markup

async def replace_link(text):
    try:
        links = await extract_link(text)

        for link in links:
            short_link = await shorteners(link)
            if short_link:
                text = text.replace(link, short_link)
    except Exception as e:
        print(f"Error converting link: {e}")

    return text

async def shorteners(link):
    if "urlshorten.in" in link:
        return await urlshorten(link)
    elif "tnshort.net" in link:
        return await tnshort(link)
    elif "TinyFy.in" in link:
        return await tinyfy(link)
    elif "tamizhmasters.net" in link:
        return await tamizhmasters(link)
    else:
        return None

async def urlshorten(url):  # sourcery skip: raise-specific-error
    # replace url domain with go.tnshort.net
    go_link = 'dl.urlshorten.in'
    ref_link = 'https://lslink.in/'
    sleep_time = 5.1
    final_domain = 'dl.urlshorten.in'
    url = url.replace(urlparse(url).netloc, final_domain)
    try:
        # client = aiohttp.ClientSession()
        async with aiohttp.ClientSession() as client:
            ref = ref_link
            h = {"referer": ref}
            # res = client.get(url, headers=h)
            async with client.get(url, headers=h) as res:
                bs4 = BeautifulSoup(await res.content.read(), "html.parser")
                inputs = bs4.find_all("input")
                data = {input.get("name"): input.get("value") for input in inputs}
                h = {
                    "content-type": "application/x-www-form-urlencoded",
                    "x-requested-with": "XMLHttpRequest",
                }
                final_url = f"https://{go_link}/links/go"
                await asyncio.sleep(sleep_time)
                # res = client.post(final_url, data=data, headers=h).json()
                async with client.post(final_url, data=data, headers=h) as res:
                    res = await res.json()
                    if res["status"] == "success":
                        return res["url"]
                    else:
                        raise Exception(
                            "Error while bypassing droplink {0}: {1}".format(
                                url, res["message"]
                            )
                        )
    except Exception as e:
        print(e)

async def tnshort(url):
    # replace url domain with go.tnshort.net
    go_link = 'go.tnshort.net'
    ref_link = 'https://usanewstoday.club/'
    sleep_time = 3.1
    final_domain = 'go.tnshort.net'
    url = url.replace(urlparse(url).netloc, final_domain)
    try:
        async with aiohttp.ClientSession() as client:
            ref = ref_link
            h = {"referer": ref}
            async with client.get(url, headers=h) as res:
                bs4 = BeautifulSoup(await res.content.read(), "html.parser")
                inputs = bs4.find_all("input")
                data = {input.get("name"): input.get("value") for input in inputs}
                h = {
                    "content-type": "application/x-www-form-urlencoded",
                    "x-requested-with": "XMLHttpRequest",
                }
                final_url = f"https://{go_link}/links/go"
                await asyncio.sleep(sleep_time)
                async with client.post(final_url, data=data, headers=h) as res:
                    res = await res.json()
                    if res["status"] == "success":
                        return res["url"]
                    else:
                        raise Exception(
                            "Error while bypassing droplink {0}: {1}".format(
                                url, res["message"]
                            )
                        )
    except Exception as e:
        return str(e)

async def tinyfy(url):
    # replace url domain with tinyfy.in
    go_link = 'tinyfy.in'
    ref_link = 'https://www.yotrickslog.tech/'
    sleep_time = 5.1
    final_domain = 'tinyfy.in'
    url = url.replace(urlparse(url).netloc, final_domain)
    try:
        async with aiohttp.ClientSession() as client:
            ref = ref_link
            h = {"referer": ref}
            async with client.get(url, headers=h) as res:
                bs4 = BeautifulSoup(await res.content.read(), "html.parser")
                inputs = bs4.find_all("input")
                data = {input.get("name"): input.get("value") for input in inputs}
                h = {
                    "content-type": "application/x-www-form-urlencoded",
                    "x-requested-with": "XMLHttpRequest",
                }
                final_url = f"https://{go_link}/links/go"
                await asyncio.sleep(sleep_time)
                async with client.post(final_url, data=data, headers=h) as res:
                    res = await res.json()
                    if res["status"] == "success":
                        return res["url"]
                    else:
                        raise Exception(
                            "Error while bypassing droplink {0}: {1}".format(
                                url, res["message"]
                            )
                        )
    except Exception as e:
        return str(e)

async def tamizhmasters(url):  # sourcery skip: raise-specific-error
    go_link = 'tamizhmasters.net'
    ref_link = 'https://azhealthlife.com/'
    sleep_time = 5.1
    final_domain = 'tamizhmasters.net'
    # replace url domain with tamizhmasters.net
    url = url.replace(urlparse(url).netloc, final_domain)
    try:
        # client = aiohttp.ClientSession()
        async with aiohttp.ClientSession() as client:
            ref = ref_link
            h = {"referer": ref}
            # res = client.get(url, headers=h)
            async with client.get(url, headers=h) as res:
                bs4 = BeautifulSoup(await res.content.read(), "html.parser")
                inputs = bs4.find_all("input")
                data = {input.get("name"): input.get("value") for input in inputs}
                h = {
                    "content-type": "application/x-www-form-urlencoded",
                    "x-requested-with": "XMLHttpRequest",
                }
                final_url = f"https://{go_link}/links/go"
                await asyncio.sleep(sleep_time)
                # res = client.post(final_url, data=data, headers=h).json()
                async with client.post(final_url, data=data, headers=h) as res:
                    res = await res.json()
                    if res["status"] == "success":
                        return res["url"]
                    else:
                        raise Exception(
                            "Error while bypassing droplink {0}: {1}".format(
                                url, res["message"]
                            )
                        )
    except Exception as e:
        print(e)
        
async def kpslink2(url):  # sourcery skip: raise-specific-error  
    go_link = 'v2.download.infotamizhan.xyz' 
    ref_link = 'https://www.infotamizhan.xyz/' 
    sleep_time = 5.1 
    final_domain = 'v2.download.infotamizhan.xyz'
    url = url.replace(urlparse(url).netloc, final_domain) 
    try: 
        # client = aiohttp.ClientSession() 
        async with aiohttp.ClientSession() as client: 
            ref = ref_link 
            h = {"referer": ref} 
            # res = client.get(url, headers=h) 
            async with client.get(url, headers=h) as res: 
                bs4 = BeautifulSoup(await res.content.read(), "html.parser") 
                inputs = bs4.find_all("input") 
                data = {input.get("name"): input.get("value") for input in inputs} 
                # filter out None
                data = {k: v for k, v in data.items() if v}
                h = { 
                    "content-type": "application/x-www-form-urlencoded", 
                    "x-requested-with": "XMLHttpRequest", 
                } 
                final_url = f"https://{go_link}/links/go" 
                await asyncio.sleep(sleep_time) 
                # res = client.post(final_url, data=data, headers=h).json() 
                async with client.post(final_url, data=data, headers=h) as res:
                    res.raise_for_status()
                    res = await res.json() 
                    if res["status"] == "success": 
                        return res["url"] 
                    else: 
                        raise Exception( 
                            "Error while bypassing droplink {0}: {1}".format( 
                                url, res["message"] 
                            ) 
                        ) 
    except Exception as e: 
        print(e)
        

#####################  Extract all urls in a string ####################
async def extract_link(string):
    regex = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
    urls = re.findall(regex, string)
    return ["".join(x) for x in urls]

async def update_stats(m:Message):
    reply_markup = str(m.reply_markup) if m.reply_markup else ''
    message = m.caption.html if m.caption else m.text.html

    short_links = await extract_link(message + reply_markup)
    total_links = len(short_links)



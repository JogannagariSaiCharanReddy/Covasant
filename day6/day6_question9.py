import asyncio 
import time, sys
import aiohttp
import requests
from bs4 import BeautifulSoup


async def download(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            return await resp.text()
            

async def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all("a",href=True)
    
async def download_all_urls(url):
    urls=[i.get("href") for i in await get_urls(url) if "http" in i.get("href") ]
    tasks= [asyncio.create_task(download(url)) for url in urls]
    res= [await task for task in tasks]
    return len(''.join(res))
    
    
    
if __name__=='__main__':
    url="http://notepadfromdas.pythonanywhere.com/pad/share"
    st=time.time()
    res = asyncio.run(download_all_urls(url)) 
    print("sucessfully downloaded using async","Time taken :",time.time()-st,"sec to download",res)
    
    
#sucessfully downloaded using async Time taken : 1.5780158042907715 sec to download 211729
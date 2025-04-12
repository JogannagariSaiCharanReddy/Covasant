import threading , time 
import concurrent.futures
import requests
from bs4 import BeautifulSoup


class download:
    def __init__(self,url):
        self.url=url
        
    def download_multiThreaded(self, ws=20):
        ex = concurrent.futures.ThreadPoolExecutor(max_workers=ws)
        res = ex.map(lambda url: requests.get(url).text,self.get_urls())
        ex.shutdown()
        return len(''.join(res))
        
    def sequential_download(self):
        res=[requests.get(url).text for url in self.get_urls()]
        return len(''.join(res))
        
        
        
    def get_urls(self):
        resp=requests.get(self.url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        urls=[a.get("href") for a in soup.find_all("a",href=True)]
        return urls



if __name__=='__main__':
    url="http://notepadfromdas.pythonanywhere.com/pad/share"
    d=download(url)
    st=time.time()
    multithread=d.download_multiThreaded()
    print("sucessfully Downloaded using multithread",multithread,"Time taken :",round(time.time()-st,2),"sec")
    d=download(url)
    st=time.time()
    sequential=d.sequential_download()
    print("sucessfully Downloaded by sequential ",sequential,"Time taken :",round(time.time()-st,2),"sec")
    
#sucessfully Downloaded using multithread 211741 Time taken : 1.65
#sucessfully Downloaded by sequential  211740 Time taken : 10.68
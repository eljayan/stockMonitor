import requests, mypaths

class Downloader:
    def __init__(self):
        self.setProxies()

    def setProxies(self):
        proxies = mypaths.PROXIES
        self.proxies = proxies

    def dowloadFile(self, url, savepath):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
        r = requests.get(url, stream=True,  proxies=self.proxies, headers=headers)
        with open(savepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 128):
                f.write(chunk)


if __name__ == '__main__':
    url = mypaths.URL
    savepath = mypaths.SAVEPATH
    d = Downloader()
    d.dowloadFile(url=url, savepath=savepath)

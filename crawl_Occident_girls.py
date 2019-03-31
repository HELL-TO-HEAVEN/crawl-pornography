# coding:utf-8
"""
user: 五根弦的吉他
time: 2019-2-2
function: 爬取色情图片
"""
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random, time, requests, re, bs4
from datetime import datetime
from io import BytesIO
from PIL import Image

class Crawl(object):

    def __init__(self):
        self.server_main = 'http://你以为我会告诉你网址吗/'
        #self.server_type = ''
        self.num = 23          # 自定义爬取页数
        self.EveryList = []
        self.PicNum = 0
        self.agent = UserAgent()
        self.headers = {'User-Agent':self.agent.random}
        # 代理池 超级粗暴！！
        self.proxies = [{"http": "http://35.193.0.225:80"},
                        {"http": "http://142.93.251.113:8080"},
                        {"http": "http://34.201.67.252:80"},
                        {"http": "http://157.230.178.46:8080"},
                        {"http": "http://142.93.177.182:8080"},
                        {"http": "http://104.248.51.135:8080"},
                        {"http": "http://68.183.20.164:8080"}
                        ]


    def alwaysGet(self, url):
        
        for i in range(10):
            URL = url
            proxy = random.choice(self.proxies)
            print('selected proxy:', proxy)

            try:
                print('now 1')
                res = requests.get(url=URL, headers=self.headers, proxies=proxy, timeout=20)
                res.close()
                
                time.sleep(random.uniform(1,2.5))
            except:

                if i==3:
                    self.proxies.remove(proxy)

                if i==9:
                    return None
                    raise ConnectionError

                print('have a rest...')
                time.sleep(random.uniform(4.0,5.5))
                continue

            else:
                print('now 2')
                res.encoding = 'gbk'
              
                self.bf = BeautifulSoup(res.text, features='lxml')

                if self.bf is None:
                    print('None again!')
                    time.sleep(random.randint(1,2))
                    continue

                return self.bf


    def GetType(self):
        bf = self.alwaysGet(self.server_main)

        if bf == None:
            return None

        div = bf.find_all('div', class_='i_tit')
        print('div:\n',div)
        bf_a = BeautifulSoup(str(div),features='lxml')
        a = bf_a.find_all('a')
        print('a:\n',a,'\nlength:',len(a))
        """
        删除下标为偶数的项
        """
        for i in range(len(a)):
            if i%2==0:
                del a[0]
            else:
                a.append(a[0])
                del a[0]

        print("final a:\n",a)
        return a


    def EnterType(self):
        self.FirstPage = self.server_main + self.GetType()[2].get('href')    # 保留这俩句
        self.EveryList.append(self.FirstPage)

    def GetNextPage(self):
        Flag=0
        bf6 = Crawl.alwaysGet(self,url=self.EveryDetailPics[-1])
        time.sleep(random.uniform(1,2))

        if bf6 is None:
            print('NoneType again!!Keep going!')
            #self.GetNextPage()
            time.sleep(random.randint(3,5))
            Crawl.GetNextPage(self)

        else:
            div = bf6.find_all('div',class_='page page_c')
            bf_a = BeautifulSoup(str(div), features='lxml')
            for each in bf_a.find_all('a'):
                if each.string=='下一页':
                    self.EveryDetailPics.append(self.FirstPage + each.get('href'))
                    Flag = True
                else: Flag = False

            if Flag==True:
                #self.GetNextPage()
                Crawl.GetNextPage(self)
            else:
                return self.EveryDetailPics



    def GetMainPics(self):

        for i in range(len(self.EveryList)):
            time.sleep(random.randint(5,9))
            print('开始爬取第 %s 页' % str(i+1))

            self.EveryMainPics = []
            self.EveryDetailPics = []

            #bf5 = self.alwaysGet(self.EveryList[i])
            bf5 = Crawl.alwaysGet(self,self.EveryList[i] )

            if bf5 is None:
                continue         # ***********

            time.sleep(1)

            print('get through 1')
            if isinstance(bf5, bs4.BeautifulSoup):            #########
                ul = bf5.find_all('ul', class_='i_pic')
                a = BeautifulSoup(str(ul), features='lxml')
                print('a.find_all(a):',a.find_all('a'))

                for each in a.find_all('a'):
                    self.EveryMainPics.append(self.server_main + each.get('href'))

                for i in range(len(self.EveryMainPics)):

                    self.EveryDetailPics.append(self.EveryMainPics[i])

                    bf2 = self.alwaysGet(self.EveryMainPics[i])

                    if bf2 is None:
                        continue                      # *************

                    time.sleep(random.uniform(1.0, 3.0))
                    div2 = bf2.find_all('div', class_='page page_c')
                    bf2_a = BeautifulSoup(str(div2), features='lxml')

                    for each2 in  bf2_a.find_all('a'):
                        if each2.string=='下一页':
                            self.EveryDetailPics.append(self.FirstPage + each2.get('href'))
                            #self.EveryDetailPics = self.GetNextPage()         ############
                            self.GetNextPage()
                            #return

                    for eachLink in self.EveryDetailPics:
                        bf3 = self.alwaysGet(eachLink)

                        if bf3 is None:
                            continue     # ********

                        time.sleep(random.uniform(1.5, 3.5))

                        try:
                            bf4 = BeautifulSoup(str(bf3.find_all('a', href="javascript:dPlayNext();")[0]), features='lxml')
                        except:
                            print('Error')
                            time.sleep(random.randint(1,2))
                            continue
                        jpg_link = bf4.find_all('img', src=re.compile(r'.jpg$'))[0]
                        JPGLINK = self.server_main + jpg_link.get('src')
                        try:
                            response = requests.get(url=JPGLINK, headers=self.headers, proxies=random.choice(self.proxies), timeout=20)
                            response.close()
                            time.sleep(random.randint(1,3))
                        except:
                            print("爬取第 %s 张图片出错" % str(self.PicNum+1))
                            time.sleep(random.uniform(4.5,7.5))
                            self.PicNum += 1
                            continue

                        try:

                            image = Image.open(BytesIO(response.content))
                            image.save('pic/%s.png' % str(self.PicNum+1))
                        except:
                            image = response.content
                            path = 'pic/%s.png' % str(self.PicNum+1)
                            with open(path,'wb') as f:
                                f.write(image)


                        self.PicNum += 1
                        print('已经爬取第 %s 张图片' % str(self.PicNum))
                        time.sleep(random.randint(1,3))


    def GetMainPage(self):

        bf7 = self.alwaysGet(self.EveryList[-1])

        if bf7 is None:
            return None

        time.sleep(random.uniform(1.0,3.5))
        div = bf7.find_all('div', class_='page page_l')
        bf_a = BeautifulSoup(str(div), features='lxml')
        for each in bf_a.find_all('a'):
            if each.string=='下一页':
                NextPageLink = self.FirstPage + each.get('href')
                self.EveryList.append(NextPageLink)
                print("length of list:",len(self.EveryList))
                time.sleep(random.randint(1,3))
                if len(self.EveryList)==self.num:                        #  自定义爬取页数
                    print("self.EveryList:", self.EveryList)
                    return self.EveryList

        print('get done')
        self.GetMainPage()

        #return self.EveryList


if __name__=='__main__':
    start = datetime.now()

    getdiv = Crawl()
    #getdiv.GetType()
    getdiv.EnterType()
    getdiv.GetMainPage()
    getdiv.GetMainPics()
    #getdiv.GetNextPage()

    end = datetime.now()
    print("Done!\nspent time:",end-start)

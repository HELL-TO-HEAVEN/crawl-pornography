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
        # 代理池
        self.proxies = [{"http": "http://35.193.0.225:80"},
                        {"http": "http://142.93.251.113:8080"},
                        {"http": "http://34.201.67.252:80"},
                        {"http": "http://157.230.178.46:8080"},
                        {"http": "http://142.93.177.182:8080"},
                        {"http": "http://104.248.51.135:8080"},
                        {"http": "http://68.183.20.164:8080"},
                        {"http": "http://165.227.107.101:8080"},
                        {"http": "http://159.65.187.217:8080"},
                        {"http": "http://142.93.62.60:8080"},
                        {"http": "http://157.230.227.144:8080"},
                        {"http": "http://68.183.20.148:8080"},
                        {"http": "http://142.93.243.157:8080"},
                        {"http": "http://3.208.230.176:8080"},
                        {"http": "http://157.230.212.82:8080"},
                        {"http": "http://157.230.8.128:8080"},
                        {"http": "http://165.155.138.176:80"},
                        {"http": "http://157.230.212.82:80"},
                        {"http": "http://159.203.178.203:8080"},
                        {"http": "http://3.17.60.126:80"},
                        {"http": "http://168.216.20.28:8080"},
                        {"http": "http://50.239.245.101:80"},
                        {"http": "http://159.203.14.121:8080"},
                        {"http": "http://138.197.128.33:8080"},
                        {"http": "http://3.17.154.4:8080"},
                        {"http": "http://157.230.236.97:80"},
                        {"http": "http://142.93.177.182:80"},
                        {"http": "http://159.65.187.217:80"},
                        {"http": "http://134.209.71.28:80"},
                        {"http": "http://192.34.63.54:8080"},
                        {"http": "http://142.93.185.187:80"},
                        {"http": "http://167.99.151.183:8080"},
                        {"http": "http://167.99.52.107:8888"},
                        {"http": "http://157.230.54.155:8080"},
                        {"http": "http://104.248.231.72:8080"},
                        {"http": "http://204.48.24.60:8080"},
                        {"http": "http://68.183.121.154:8080"},
                        {"http": "http://157.230.186.27:8080"},
                        {"http": "http://104.248.236.12:8080"},
                        {"http": "http://3.95.193.173:80"},
                        {"http": "http://68.183.53.127:8080"},
                        {"http": "http://3.17.60.126:8080"},
                        {"http": "http://3.90.126.3:8080"},
                        {"http": "http://134.209.115.86:8080"},
                        {"http": "http://134.209.38.212:8080"},
                        {"http": "http://157.230.179.73:8080"},
                        {"http": "http://157.230.236.97:8080"},
                        {"http": "http://157.230.8.35:8080"},
                        {"http": "http://68.183.137.143:8080"},
                        {"http": "http://68.183.159.134:80"},
                        {"http": "http://134.209.123.111:8080"},
                        {"http": "http://3.93.151.128:8080"},
                        {"http": "http://134.209.66.166:8080"},
                        {"http": "http://138.197.155.142:8080"},
                        {"http": "http://54.156.183.45:80"},
                        {"http": "http://138.68.57.160:8080"},
                        {"http": "http://38.21.243.247:1080"},
                        {"http": "http://162.211.126.220:443"},
                        {"http": "http://65.49.196.26:8888"},
                        {"http": "http://165.227.62.167:8080"},
                        {"http": "http://104.248.190.115:8080"},
                        {"http": "http://134.209.52.62:8080"},
                        {"http": "http://178.128.179.63:8080"},
                        {"http": "http://64.33.171.19:8080"},
                        {"http": "http://206.189.216.141:8080"},
                        {"http": "http://138.68.57.160:80"},
                        {"http": "http://165.227.62.167:80"},
                        {"http": "http://178.128.65.42:8080"},
                        {"http": "http://13.56.2.56:8090"},
                        {"http": "http://168.216.24.246:8080"},
                        {"http": "http://204.29.115.149:8080"},
                        {"http": "http://149.56.1.37:8080"},
                        {"http": "http://34.73.62.46:80"},
                        {"http": "http://68.183.143.161:8080"},
                        {"http": "http://67.63.33.7:80"},
                        {"https": "https://35.193.0.225:80"},
                        {"http": "http://165.138.225.250:8080"},
                        {"http": "http://45.113.69.177:1080"},
                        {"http": "http://159.203.14.121:80"},
                        {"http": "http://142.93.206.254:80"},
                        {"http": "http://34.73.62.46:8080"},
                        {"http": "http://35.185.44.176:8080"},
                        {"http": "http://159.89.119.45:8080"},
                        {"http": "http://45.79.194.42:31280"},
                        {"http": "http://71.29.61.211:80"},
                        {"http": "http://206.189.162.192:8080"},
                        {"http": "http://159.203.19.216:8080"},
                        {"http": "http://165.227.42.21:8080"},
                        {"http": "http://168.11.14.250:8009"},
                        {"http": "http://142.93.24.225:8080"},
                        {"http": "http://157.230.150.101:8080"},
                        {"http": "http://163.153.214.50:8080"},
                        {"https": "https://68.183.20.164:8080"},
                        {"https": "https://104.248.231.72:8080"},
                        {"https": "https://157.230.8.128:8080"},
                        {"http": "http://104.167.5.82:8080"},
                        {"https": "https://168.216.20.28:8080"},
                        {"https": "https://68.183.143.161:8080"},
                        {"https": "https://165.155.138.176:80"},
                        {"https": "https://104.248.236.12:8080"},
                        {"https": "https://138.197.128.33:8080"},
                        {"https": "https://168.216.24.246:8080"},
                        {"https": "https://3.17.154.4:8080"},
                        {"https": "https://3.93.151.128:8080"},
                        {"https": "https://157.230.8.35:8080"},
                        {"https": "https://167.99.151.183:8080"},
                        {"https": "https://68.183.121.154:8080"},
                        {"https": "https://167.99.52.107:8888"},
                        {"https": "https://71.29.61.211:80"},
                        {"https": "https://159.89.119.45:8080"},
                        {"https": "https://45.79.194.42:31280"},
                        {"https": "https://206.189.216.141:8080"},
                        {"https": "https://165.227.42.21:8080"},
                        {"https": "https://159.203.19.216:8080"},
                        {"http": "http://184.185.166.27:8080"},
                        {"https": "https://163.153.214.50:8080"},
                        {"https": "https://168.11.14.250:8009"},
                        {"http": "http://207.10.243.26:8080"},
                        {"http": "http://167.99.7.198:8080"},
                        {"http": "http://47.90.251.141:8888"},
                        {"http": "http://159.16.106.110:80"},
                        {"https": "https://157.230.150.101:8080"},
                        {"http": "http://209.97.177.138:8080"},
                        {"https": "https://97.64.135.4:8080"},
                        {"http": "http://54.39.23.81:8082"},
                        {"https": "https://206.189.162.192:8080"},
                        {"http": "http://178.62.29.166:8080"},
                        {"http": "http://178.62.39.65:8080"},
                        {"https": "https://54.156.183.45:80"},
                        {"http": "http://178.62.27.132:8080"},
                        {"http": "http://178.128.162.132:8080"},
                        {"http": "http://54.39.98.135:80"},
                        {"http": "http://142.93.143.74:8080"},
                        {"http": "http://18.196.1.243:8081"},
                        {"http": "http://178.62.210.107:8080"},
                        {"http": "http://142.93.37.75:8080"},
                        {"https": "https://104.167.5.82:8080"},
                        {"http": "http://206.189.123.87:8080"},
                        {"http": "http://167.99.33.184:8080"},
                        {"http": "http://37.59.248.187:1080"},
                        {"http": "http://51.77.229.143:8080"},
                        {"http": "http://159.65.92.98:8080"},
                        {"http": "http://178.128.168.122:8080"},
                        {"http": "http://62.7.85.234:8080"},
                        {"http": "http://142.93.132.238:8080"},
                        {"http": "http://142.93.141.131:8888"},
                        {"http": "http://191.102.83.146:80"},
                        {"http": "http://35.176.201.28:80"},
                        {"http": "http://201.147.242.186:8080"},
                        {"http": "http://157.230.19.240:80"},
                        {"https": "https://184.185.166.27:8080"},
                        {"https": "https://54.39.23.81:8082"},
                        {"https": "https://159.16.106.110:80"},
                        {"http": "http://207.180.233.72:80"},
                        {"http": "http://35.185.201.225:8080"},
                        {"http": "http://46.101.120.137:8080"},
                        {"http": "http://178.33.148.177:8080"},
                        {"http": "http://94.177.241.9:80"},
                        {"http": "http://173.249.33.139:8888"},
                        {"http": "http://46.101.157.124:8080"},
                        {"http": "http://163.172.220.221:8888"},
                        {"http": "http://62.210.73.153:54321"},
                        {"http": "http://37.59.248.189:1080"},
                        {"http": "http://47.89.249.166:80"},
                        {"https": "https://209.97.177.138:8080"},
                        {"http": "http://173.72.102.246:80"},
                        {"http": "http://185.74.235.222:8080"},
                        {"http": "http://200.69.82.100:999"},
                        {"https": "https://178.62.39.65:8080"},
                        {"http": "http://163.172.28.22:80"},
                        {"http": "http://90.145.221.186:80"},
                        {"http": "http://54.233.188.211:80"},
                        {"http": "http://142.93.96.177:80"},
                        {"http": "http://51.75.65.79:8080"},
                        {"http": "http://178.33.9.97:1080"},
                        {"http": "http://178.33.9.98:1080"},
                        {"http": "http://138.117.4.45:80"},
                        {"http": "http://167.99.237.166:8888"},
                        {"http": "http://64.235.35.128:8888"},
                        {"https": "https://178.128.162.132:8080"},
                        {"https": "https://142.93.37.75:8080"},
                        {"https": "https://142.93.143.74:8080"},
                        {"http": "http://31.184.252.69:443"},
                        {"http": "http://18.231.190.109:8080"},
                        {"http": "http://80.211.70.126:8080"},
                        {"http": "http://62.138.16.55:443"},
                        {"http": "http://80.211.110.138:8080"},
                        {"http": "http://94.242.59.135:10010"},
                        {"http": "http://94.242.59.135:1448"},
                        {"http": "http://94.242.58.142:10010"},
                        {"https": "https://18.196.1.243:8081"},
                        {"https": "https://178.62.210.107:8080"},
                        {"https": "https://35.164.193.94:8080"},
                        {"https": "https://201.147.242.186:8080"},
                        {"https": "https://142.93.132.238:8080"},
                        {"https": "https://51.77.229.143:8080"},
                        {"https": "https://142.93.141.131:8888"},
                        {"https": "https://159.65.92.98:8080"},
                        {"https": "https://178.128.168.122:8080"},
                        {"https": "https://167.99.237.166:8888"},
                        {"https": "https://64.235.35.128:8888"},
                        {"https": "https://167.99.33.184:8080"},
                        {"https": "https://62.210.73.153:54321"},
                        {"http": "http://35.164.193.94:8080"},
                        {"https": "https://178.33.148.177:8080"},
                        {"https": "https://62.7.85.234:8080"},
                        {"https": "https://173.249.33.139:8888"},
                        {"https": "https://163.172.220.221:8888"},
                        {"https": "https://207.180.233.72:80"},
                        {"https": "https://46.101.157.124:8080"},
                        {"https": "https://51.75.65.79:8080"},
                        {"http": "http://178.128.151.27:80"},
                        {"https": "https://178.62.215.15:8888"},
                        {"https": "https://31.184.252.69:443"},
                        {"https": "https://94.242.58.142:10010"},
                        {"http": "http://162.144.220.192:80"},
                        {"https": "https://94.242.59.135:1448"},
                        {"http": "http://77.95.96.169:80"},
                        {"http": "http://85.214.128.137:2467"},
                        {"http": "http://94.177.215.30:80"},
                        {"https": "https://62.138.16.55:443"},
                        {"http": "http://54.92.2.147:8082"},
                        {"http": "http://188.173.32.55:8888"},
                        {"http": "http://212.101.74.68:443"},
                        {"http": "http://93.88.75.31:8080"},
                        {"http": "http://212.101.74.78:443"},
                        {"http": "http://78.47.151.98:8888"},
                        {"http": "http://40.131.73.230:8080"},
                        {"http": "http://77.59.248.61:8080"},
                        {"http": "http://94.242.58.14:10010"},
                        {"http": "http://94.242.57.136:10010"},
                        {"http": "http://94.242.58.142:1448"},
                        {"http": "http://158.255.47.211:8081"},
                        {"http": "http://190.2.146.80:80"},
                        {"http": "http://158.255.47.215:8081"},
                        {"http": "http://80.211.103.18:8080"},
                        {"http": "http://212.237.52.148:8080"},
                        {"http": "http://190.0.18.180:9991"},
                        {"http": "http://178.128.49.98:8080"},
                        {"http": "http://193.222.202.237:80"},
                        {"http": "http://213.234.31.127:8080"},
                        {"http": "http://176.106.229.51:8080"},
                        {"http": "http://191.252.201.96:80"},
                        {"http": "http://136.243.211.106:80"},
                        {"http": "http://201.64.22.50:8081"},
                        {"http": "http://66.97.37.63:80"},
                        {"http": "http://66.97.38.150:80"},
                        {"http": "http://66.97.37.55:80"},
                        {"http": "http://191.252.195.210:8080"},
                        {"http": "http://213.247.197.105:8080"},
                        {"http": "http://190.114.253.63:8080"},
                        {"http": "http://217.9.95.201:8080"},
                        {"http": "http://191.240.152.128:80"},
                        {"http": "http://46.44.53.105:8081"},
                        {"http": "http://95.140.27.135:33727"},
                        {"http": "http://128.140.225.49:80"},
                        {"http": "http://93.120.156.77:8080"},
                        {"http": "http://119.196.18.51:8080"},
                        {"http": "http://66.97.34.12:80"},
                        {"http": "http://187.16.4.108:8080"},
                        {"http": "http://66.97.38.58:80"},
                        {"http": "http://188.225.9.121:8080"},
                        {"http": "http://186.64.120.236:8080"},
                        {"http": "http://186.64.122.198:80"},
                        {"http": "http://170.239.84.24:8080"},
                        {"http": "http://168.232.165.236:8080"},
                        {"http": "http://34.95.75.141:8080"},
                        {"http": "http://66.97.38.87:80"},
                        {"http": "http://81.5.103.14:8081"},
                        {"http": "http://66.97.37.52:80"},
                        {"http": "http://35.199.104.209:80"},
                        {"http": "http://94.242.58.14:1448"},
                        {"http": "http://84.210.238.216:80"},
                        {"http": "http://200.175.206.116:8080"},
                        {"http": "http://201.148.127.58:31280"},
                        {"http": "http://91.187.93.166:80"},
                        {"http": "http://189.85.89.110:80"},
                        {"http": "http://191.243.23.68:47578"},
                        {"http": "http://212.150.53.77:80"},
                        {"http": "http://190.104.8.19:8080"},
                        {"http": "http://212.150.53.75:80"},
                        {"http": "http://212.101.74.79:443"},
                        {"http": "http://200.255.122.174:8080"},
                        {"http": "http://200.255.122.170:8080"},
                        {"http": "http://212.101.74.76:443"},
                        {"http": "http://54.233.188.211:8080"},
                        {"http": "http://190.186.58.185:65301"},
                        {"http": "http://186.96.121.164:30868"},
                        {"http": "http://92.222.14.209:9999"},
                        {"https": "https://72.35.40.34:8080"},
                        {"http": "http://134.119.214.195:8080"},
                        {"http": "http://182.253.149.4:8888"},
                        {"http": "http://196.13.208.23:8080"},
                        {"http": "http://128.199.196.140:31330"},
                        {"http": "http://94.69.206.246:8080"},
                        {"http": "http://134.119.205.164:8080"},
                        {"http": "http://120.194.18.90:81"},
                        {"http": "http://111.223.75.178:8080"},
                        {"https": "https://94.242.59.135:10010"},
                        {"http": "http://128.199.246.226:8080"},
                        {"http": "http://178.128.114.91:31330"},
                        {"http": "http://12.106.88.164:8080"},
                        {"http": "http://128.199.203.59:31330"},
                        {"http": "http://128.199.143.156:31330"},
                        {"http": "http://94.205.140.158:56521"},
                        {"http": "http://49.173.19.220:443"},
                        {"http": "http://128.199.143.65:31330"},
                        {"http": "http://45.255.126.33:80"},
                        {"http": "http://41.73.15.246:80"},
                        {"http": "http://159.138.22.112:80"},
                        {"http": "http://41.73.15.130:80"},
                        {"http": "http://119.28.203.242:8000"},
                        {"http": "http://119.28.31.29:8888"},
                        {"http": "http://171.255.192.118:8080"},
                        {"http": "http://113.254.44.242:8383"},
                        {"http": "http://51.38.71.101:8080"},
                        {"http": "http://35.241.65.18:80"},
                        {"http": "http://213.6.7.53:80"},
                        {"http": "http://211.23.149.28:80"},
                        {"http": "http://118.190.95.35:9001"},
                        {"http": "http://178.93.39.176:46432"},
                        {"http": "http://175.116.74.123:80"},
                        {"http": "http://103.228.117.244:8080"},
                        {"http": "http://178.128.61.80:8080"},
                        {"http": "http://85.237.46.168:51846"},
                        {"http": "http://52.79.128.193:80"},
                        {"http": "http://85.237.54.35:8081"},
                        {"http": "http://117.121.213.80:8080"},
                        {"http": "http://83.13.205.178:8080"},
                        {"http": "http://150.109.198.207:1080"},
                        {"http": "http://66.97.35.241:80"},
                        {"http": "http://47.52.27.97:31280"},
                        {"http": "http://200.152.68.54:80"},
                        {"http": "http://31.173.90.110:8080"},
                        {"http": "http://206.189.42.126:8080"},
                        {"http": "http://190.97.120.10:80"},
                        {"http": "http://168.232.165.236:80"},
                        {"http": "http://128.199.84.155:8080"},
                        {"http": "http://78.85.174.164:8081"},
                        {"http": "http://178.128.215.199:8080"},
                        {"http": "http://94.180.112.180:8081"},
                        {"http": "http://213.6.7.49:80"},
                        {"http": "http://213.6.7.52:80"},
                        {"http": "http://46.29.195.210:8080"},
                        {"http": "http://201.48.194.210:80"},
                        {"http": "http://118.99.103.14:8080"},
                        {"http": "http://23.102.224.85:80"},
                        {"http": "http://103.249.182.20:80"},
                        {"http": "http://119.28.118.116:1080"},
                        {"http": "http://206.189.154.182:8080"},
                        {"http": "http://178.128.31.153:8080"},
                        {"http": "http://134.209.108.243:8080"},
                        {"http": "http://170.81.163.13:34809"},
                        {"http": "http://187.181.132.107:8080"},
                        {"http": "http://45.238.54.103:8088"},
                        {"http": "http://83.169.208.183:60938"},
                        {"http": "http://1.10.186.240:52005"},
                        {"http": "http://223.111.254.83:80"},
                        {"http": "http://62.133.156.37:61758"},
                        {"http": "http://201.217.247.99:80"},
                        {"http": "http://176.53.2.122:8080"},
                        {"http": "http://37.252.64.73:42517"},
                        {"http": "http://200.105.170.52:53512"},
                        {"http": "http://111.230.113.238:9999"},
                        {"http": "http://209.97.166.49:31330"},
                        {"http": "http://88.82.73.242:30780"},
                        {"http": "http://134.119.207.9:8080"},
                        {"http": "http://173.249.35.163:10010"},
                        {"https": "https://190.0.18.180:9991"},
                        {"https": "https://186.96.121.164:30868"},
                        {"https": "https://40.131.73.230:8080"},
                        {"http": "http://196.13.208.22:8080"},
                        {"http": "http://58.65.129.25:57805"},
                        {"http": "http://193.200.151.69:42756"},
                        {"http": "http://178.128.27.180:8080"},
                        {"https": "https://78.47.151.98:8888"},
                        {"https": "https://190.186.58.185:65301"},
                        {"https": "https://91.187.93.166:80"},
                        {"https": "https://40.68.149.233:8080"},
                        {"https": "https://188.173.32.55:8888"},
                        {"https": "https://212.150.53.75:80"},
                        {"https": "https://187.16.4.108:8080"},
                        {"http": "http://213.6.7.51:80"},
                        {"https": "https://170.81.163.13:34809"},
                        {"https": "https://95.140.27.135:33727"},
                        {"https": "https://85.214.128.137:2467"},
                        {"https": "https://94.242.57.136:10010"},
                        {"http": "http://157.230.2.100:8080"},
                        {"http": "http://134.209.119.237:8080"},
                        {"https": "https://94.242.58.14:10010"},
                        {"https": "https://94.242.58.14:1448"},
                        {"http": "http://78.40.87.18:808"},
                        {"http": "http://197.159.43.25:8080"},
                        {"https": "https://92.222.14.209:9999"},
                        {"https": "https://51.38.71.101:8080"},
                        {"https": "https://176.106.229.51:8080"},
                        {"https": "https://178.93.39.176:46432"},
                        {"https": "https://85.237.46.168:51846"},
                        {"https": "https://93.120.156.77:8080"},
                        {"https": "https://217.9.95.201:8080"},
                        {"https": "https://77.59.248.61:8080"},
                        {"http": "http://178.128.16.237:31330"},
                        {"http": "http://198.1.122.29:80"},
                        {"https": "https://200.255.122.170:8080"},
                        {"https": "https://200.255.122.174:8080"},
                        {"http": "http://218.57.146.212:8888"},
                        {"https": "https://200.152.68.54:80"},
                        {"https": "https://201.48.194.210:80"},
                        {"https": "https://213.247.197.105:8080"},
                        {"https": "https://191.252.201.96:80"},
                        {"https": "https://200.175.206.116:8080"},
                        {"https": "https://190.104.8.19:8080"},
                        {"http": "http://104.248.135.32:8080"},
                        {"https": "https://83.169.208.183:60938"},
                        {"https": "https://62.133.156.37:61758"},
                        {"https": "https://46.29.195.210:8080"},
                        {"https": "https://173.249.35.163:10010"},
                        {"https": "https://128.199.84.155:8080"},
                        {"https": "https://128.199.246.226:8080"},
                        {"https": "https://206.189.42.126:8080"},
                        {"https": "https://128.199.196.140:31330"},
                        {"https": "https://128.199.143.156:31330"},
                        {"https": "https://178.128.114.91:31330"},
                        {"https": "https://128.199.203.59:31330"},
                        {"https": "https://128.199.143.65:31330"},
                        {"https": "https://178.128.31.153:8080"},
                        {"https": "https://134.209.108.243:8080"},
                        {"https": "https://201.64.22.50:8081"},
                        {"https": "https://49.173.19.220:443"},
                        {"https": "https://94.205.140.158:56521"},
                        {"https": "https://190.114.253.63:8080"},
                        {"https": "https://201.71.145.245:8080"},
                        {"https": "https://119.196.18.51:8080"},
                        {"http": "http://109.111.232.237:6666"},
                        {"https": "https://189.85.89.110:80"},
                        {"http": "http://54.251.38.138:8080"},
                        {"http": "http://134.119.214.203:8080"},
                        {"http": "http://178.128.114.34:31330"},
                        {"http": "http://128.199.203.207:31330"},
                        {"http": "http://178.128.107.51:31330"},
                        {"http": "http://89.22.175.42:8080"},
                        {"http": "http://103.75.225.34:80"},
                        {"http": "http://103.73.149.5:80"},
                        {"http": "http://211.24.102.168:80"},
                        {"http": "http://197.216.2.14:8080"},
                        {"http": "http://197.216.2.9:8080"},
                        {"http": "http://211.24.102.171:80"},
                        {"http": "http://128.199.203.117:31330"},
                        {"http": "http://121.40.138.161:8000"},
                        {"http": "http://128.199.145.143:31330"},
                        {"https": "https://37.252.64.73:42517"},
                        {"http": "http://178.169.64.76:8081"},
                        {"http": "http://13.127.244.13:80"},
                        {"http": "http://128.199.204.172:31330"},
                        {"http": "http://47.52.56.18:80"},
                        {"http": "http://128.199.170.87:31330"},
                        {"http": "http://128.199.195.225:31330"},
                        {"http": "http://178.128.25.230:31330"},
                        {"http": "http://165.21.89.59:80"},
                        {"http": "http://128.199.194.79:31330"},
                        {"http": "http://128.199.144.66:31330"},
                        {"http": "http://128.199.203.26:31330"},
                        {"http": "http://178.128.24.113:31330"},
                        {"http": "http://128.199.201.155:31330"},
                        {"http": "http://128.199.203.167:31330"},
                        {"http": "http://128.199.196.88:31330"},
                        {"http": "http://128.199.143.93:31330"},
                        {"http": "http://210.5.96.178:8080"},
                        {"http": "http://80.237.54.158:8080"},
                        {"http": "http://128.199.201.183:31330"},
                        {"http": "http://178.128.107.254:31330"},
                        {"http": "http://178.128.94.234:31330"},
                        {"http": "http://128.199.196.45:31330"},
                        {"http": "http://178.128.107.73:31330"},
                        {"http": "http://178.128.105.138:31330"},
                        {"https": "https://94.69.206.246:8080"},
                        {"http": "http://177.125.119.5:8080"},
                        {"http": "http://41.139.159.34:51589"},
                        {"http": "http://213.221.57.214:53281"},
                        {"http": "http://191.253.109.88:8080"},
                        {"http": "http://179.97.27.49:30785"},
                        {"http": "http://41.50.81.40:60170"},
                        {"http": "http://202.29.210.166:57603"},
                        {"http": "http://185.190.40.75:8080"},
                        {"https": "https://125.167.42.84:8080"},
                        {"https": "https://178.128.215.199:8080"},
                        {"http": "http://128.201.97.247:8030"},
                        ]


    def alwaysGet(self, url):
        
        for i in range(10):
            URL = url
            print('URL1:', URL)
            proxy = random.choice(self.proxies)
            print('selected proxy:', proxy)

            try:
                print('now 1')
                res = requests.get(url=URL, headers=self.headers, proxies=proxy, timeout=20)
                res.close()
                print('get through it')
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
                # print('+++++++++++++++++++++++++++++res.text:\n',res.text)
                #print('-/-/-/-/--/-/----/-/--/----/---/-/--res.text:',res.text)
                self.bf = BeautifulSoup(res.text, features='lxml')

                print("***************************type of bf:", type(self.bf))

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


        """
        bf = self.alwaysGet(self.FirstPage)
        ul = bf.find_all('ul',class_='i_pic')
        a = BeautifulSoup(str(ul), features='lxml')

        return a .find_all('a')
        """


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
            print('#################### self.EveryDetailPics[-1]:',self.EveryDetailPics[-1])
            print('00000000000000000000000000 type of bf6:',type(bf6))
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
                print('self.EveryDetailPics:',self.EveryDetailPics)
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

            print("55555555555555555555555555  type of bf5:", type(bf5))

            print('get through 1')
            if isinstance(bf5, bs4.BeautifulSoup):            #########
                ul = bf5.find_all('ul', class_='i_pic')
                a = BeautifulSoup(str(ul), features='lxml')
                print('a.find_all(a):',a.find_all('a'))

                for each in a.find_all('a'):
                    self.EveryMainPics.append(self.server_main + each.get('href'))

                print("EveryMainPics:",self.EveryMainPics)


                for i in range(len(self.EveryMainPics)):

                    self.EveryDetailPics.append(self.EveryMainPics[i])

                    bf2 = self.alwaysGet(self.EveryMainPics[i])

                    if bf2 is None:
                        continue                      # *************

                    time.sleep(random.uniform(1.0, 3.0))
                    print('get through 2')
                    div2 = bf2.find_all('div', class_='page page_c')
                    bf2_a = BeautifulSoup(str(div2), features='lxml')

                    for each2 in  bf2_a.find_all('a'):
                        if each2.string=='下一页':
                            self.EveryDetailPics.append(self.FirstPage + each2.get('href'))
                            #self.EveryDetailPics = self.GetNextPage()         ############
                            self.GetNextPage()
                            print('Print again self.EverydetailPics',self.EveryDetailPics)
                            #return

                    for eachLink in self.EveryDetailPics:
                        bf3 = self.alwaysGet(eachLink)

                        if bf3 is None:
                            continue     # ********

                        time.sleep(random.uniform(1.5, 3.5))
                        print('get through 3')
                        print('+++++++++++++++++++++++++bf3:\n',bf3.prettify())
                        try:
                            bf4 = BeautifulSoup(str(bf3.find_all('a', href="javascript:dPlayNext();")[0]), features='lxml')
                        except:
                            print('有问题')
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
        print('%%%%%%%%%%%%%%%%%%%%%%% type of bf:',type(bf7))
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

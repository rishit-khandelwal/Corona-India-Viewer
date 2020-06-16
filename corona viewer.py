from requests import get
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

text = get('https://www.mygov.in/covid-19').text

soup = BeautifulSoup(text,'html.parser')

data = ''

for div_inf in soup.find_all('div',attrs={'class': 'iblock'}):
     t = div_inf.text.replace('\n','')
     if t[0] == ' ':
          t = t[1:]
     
     x = t
     b = ''
     c = ''
     for i in x:
          try:
               a = int(i)
               b += str(a)
          except:
               c += i

     data += b+'.'+c+'!'
     
print(data,file=open('Coronafile','a'))

import time

d= []
with open('datefile','a') as f:
     tm = time.localtime()
     month = tm.tm_mon
     day = tm.tm_mday
     mint = tm.tm_min
     sec = tm.tm_sec
     hour = tm.tm_hour
     print(str(month)+'.'+str(day)+str(sec)+str(mint)+str(hour),file=f)
     


with open('Coronafile') as f:
     m = '' 
     for b in f.readlines():
          for a in b:
               if a != '\n' and a != ' ':
                    m += a
          m += '\n'
     
     for x in m.split('\n'):
          try:
               d.append(int(x.split('!',1)[0].split('.')[0]))
          except:
               pass
     
import numpy as np

y = np.array(d)

s = y.size

with open('datefile') as f:
     sam = []
     for a in f.readlines():
          sam.append(a)
     print(sam)
     x = np.array(sam)
try:
     plt.plot(x,y,'g-')
except :
     print('error')

plt.tight_layout()
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')
plt.show()

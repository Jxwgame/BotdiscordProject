from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

#-URL ออกมาเป็นbyte
url = 'https://www.tmd.go.th/forecast/daily'

#-request URL
web_req = req(url)
page_html = web_req.read()
web_req.close()

#print(page_html)

#-Convert page_html to Soup Object 
data = soup(page_html,'html.parser')
#print(data) #view page sroce

#-Find Element (td:'')
temp = data.findAll('p',{'class':'sub-content'})
#print((temp))

province = data.findAll('p',{'class','sub-title'})

print('พยากรณ์อากาศสำหรับประเทศไทย18:00 น. วันนี้ ถึง 18:00 น. วันพรุ่งนี้\n')
for i in range(0,7):
    result_temp = temp[i].text.replace(' ','') #data
    result_pv = province[i].text.replace(' ','') #position
    print('{} : {}'.format(result_pv,result_temp))
    
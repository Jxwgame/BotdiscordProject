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

result_temp = temp[0].text.replace(' ','') #data
result_pv = province[0].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))

result_temp = temp[1].text.replace(' ','') #data
result_pv = province[1].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))

result_temp = temp[2].text.replace(' ','') #data
result_pv = province[2].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))

result_temp = temp[3].text.replace(' ','') #data
result_pv = province[3].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))

result_temp = temp[4].text.replace(' ','') #data
result_pv = province[4].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))

result_temp = temp[5].text.replace(' ','') #data
result_pv = province[5].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))

result_temp = temp[6].text.replace(' ','') #data
result_pv = province[6].text.replace(' ','') #position
print('{} : {}'.format(result_pv,result_temp))
    
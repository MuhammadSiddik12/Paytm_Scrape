# from requests import get
# from bs4 import BeautifulSoup as b
# from pprint import pprint
# import time,json
# list2=[]

# def Data_():
#     list1=[]
#     for k in range(11):
#         d={}
#         page=get('https://paytmmall.com/shop/search?q=mango%20pickle&from=organic&child_site_id=6&site_id=2&c&page='+str(k))
#         soup=b(page.content,'html.parser')
#         main=soup.find('div',class_='_3RA-')
#         for i in main:
#             list1.append('https://paytmmall.com/'+i.find('a')['href'])
#     return list1
# def full_info(list1):
#     d={}
#     for i in list1:
#         page=get(i)
#         soup=b(page.content,'html.parser')
#         d['name']=soup.find('h1',class_='NZJI').text
#         d['price']=f"Rs: {soup.find('span',class_='_1V3w').text}"
#         d['img_link']=soup.find('div',class_="_1-Zc").img['alt']
#         d['product_type']=soup.find('div',class_="wJuG _1CXW").find('div',class_='_2LOI').a.text
#         da=soup.find('div',class_="wJuG _1CXW").findAll('div',class_='_2LOI')[-2].text
#         if '2021' in da:
#             d['expiry_date']=da
#         else:
#             continue
#         d['brand']=soup.find('div',class_="wJuG _1CXW").findAll('div',class_='_2LOI')[1].text
#         capacity =soup.find('div',class_="wJuG _1CXW").findAll('div',class_='_2LOI')[4].text
#         if 'g' in capacity or 'kg' in capacity and len(capacity)<7:
#             d['capacity']=capacity
#         list2.append(d.copy())
#     with open('paytm.json','w') as fi:
#         fi.write(json.dumps(list2,indent=4))
#         fi.close()
# full_info(Data_())


from selenium import webdriver
# import os,requests,json
# import time
# from bs4 import BeautifulSoup as bs
# link_list=[]
# driver = webdriver.Chrome('/home/muhammad_siddik_akbar/Desktop/chromedriver')
# driver.get('https://paytmmall.com/shop/search?q=mango%20pickle& from=organic&child_site_id=6&site_id=2&c')
# d=driver.find_elements_by_css_selector('#app > div > div._2Bze > div > div > div._1Qd6 > div > div._1FqI > div._2ACe > div.kYTG > i')

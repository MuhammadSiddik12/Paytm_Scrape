# from requests import get
# from bs4 import BeautifulSoup as b
# from pprint import pprint
# import time
# name=[]
# price=[]
# img=[]
# page_=[]
# dis=[]
# for k in range(11):
#     page=get('https://paytmmall.com/shop/search?q=mango%20pickle&from=organic&child_site_id=6&site_id=2&c&page='+str(k))
#     soup=b(page.content,'html.parser')
#     body=soup.find('body')
#     main=body.find('div',class_='_3RA-')
#     for i in main:
#         page_.append('https://paytmmall.com/'+i.find('a')['href'])
#         img.append(i.find('div',class_='_3nWP').find('img')['src'])
#         name.append(i.find('div',class_="UGUy").text)
#         price.append(f"Rs: {i.find('span').text}")
#         p=i.find('span',class_='c-ax')
#         if p == None:
#             continue
#         else:
#             dis.append(p.text[1:])
# # print(len(name))
# # print(len(price))
# # print(len(img))
# # print(len(page_))
# # print(len(dis))
# with open('main.html','w') as d:
#     d.write('''
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Document</title>
# </head>
# <body>
#     <h1>
#     <center>Welcome To Shopping Mall</center>
#     </h1>
# </body>''')
#     for m in range(len(dis)):
#         d.write(f"""
#         <body>
#             <a href={page_[m]}></a>
#             <img src={img[m]}
#             width=145" height="310">
#             <h2>{'Brand --> '}
#                 {name[m]}
#             </h2>
#             <h2>{'Price --> '}
#             {price[m]}</h2>
#             <h2>{'Discount --> '}
#             {dis[m]}</h2>
#         </body>
#         </html>""")
#     d.close()
        
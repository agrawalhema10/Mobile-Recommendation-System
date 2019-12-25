import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

class scrap:
    def __init__(self,mobile_name):
        self.mobile_name=mobile_name
    def func(self,mobile_name):
        try:
            myurl=f"https://pricebaba.com/mobile/{mobile_name}"
            uClient=uReq(myurl)
            page_soup=soup(uClient,'html.parser')
            d=page_soup.find('div',{"id":"inventory"})
            g=d.find('div',{"id":"onlineInventoryCnt"})
            main_compare=g.find_all('div',{"br-b-1 invt__list-itm inventoryListItem"})
            d={}
            final=[]
            if(main_compare==[]):
                message=g.find('div',{"p-xl txt-al-c"})
                return message.text
            else:
                for x in main_compare:
                    sh=[]
                    l1=""
                    l2=""
                    l3=""
                    l4=""
                    y=x.find('div',{"stack-inline--rigid p-t-m p-h-m"})
                    l=y.find_all('div',{"col-2 flt-l v-al-top p-h-xs"})
                    lni=l[0].find('div',{"txt-al-l"})
                    link=lni.find('a',{})
                    image=lni.find('img',{})
                    l1=link['href']
                    l2=image['src']
                    l3=image['alt']
                    f=l[1].find('li',{"m-v-xs"})
                    price=f.find('span',{"invt__prc txt-clr-light-black txt-wt-m"})
                    try:
                        l4=price.text
                    except AttributeError as e:
                        l4="-"
                    sh.append(l1)
                    sh.append(l2)
                    sh.append(l3)
                    sh.append(l4)
                    final.append(sh)
            return final
        except :
            return "Wrong Name"


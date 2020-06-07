from flask import  Flask,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def shopno_beef():
    beef_url=requests.get("https://www.shwapno.com/products/meat--fish-meat-beef/other/beef-premium-per-kg-(--100gm)/pid-12100254.aspx?vpid=9097914").text
    soup=BeautifulSoup(beef_url,'lxml')
    title="Beef Premium per Kg (+/- 100gm) 1 Kg"
    quantity="1kg"
    price_amounts=soup.select("#lblOfferPrice >span")
    price=price_amounts[1].text
    beef_dict1={}
    beef_dict1['title']=title
    beef_dict1['quantity']=quantity
    beef_dict1['price']=price
    return beef_dict1


def shopno_beef_item2():
    beef_url2=requests.get("https://www.shwapno.com/products/meat--fish-meat-beef/other/beef-minced-premium-(keema)/pid-12100250.aspx?vpid=9098006").text
    soup=BeautifulSoup(beef_url2,'lxml')
    title="Beef Minced Premium (keema) 1 Kg"
    quantity="1kg"
    price_amounts=soup.select("#lblOfferPrice >span")
    price=price_amounts[1].text
    beef_dict2={}
    beef_dict2['title']=title
    beef_dict2['quantity']=quantity
    beef_dict2['price']=price
    return beef_dict2

def shopno_beef_item3():
    beef_url3=requests.get("https://www.shwapno.com/products/meat--fish-meat-beef/na/beef-premium-(special-offer)/pid-15716003.aspx").text
    soup=BeautifulSoup(beef_url3,'lxml')
    title="Beef Premium (Special Offer) "
    quantity="1kg"
    price_amounts=soup.select("#lblOfferPrice >span")
    price=price_amounts[1].text
    beef_dict3={}
    beef_dict3['title']=title
    beef_dict3['quantity']=quantity
    beef_dict3['price']=price
    return beef_dict3

def chaldal_beef():
    beef_url=requests.get("https://chaldal.com/bengal-meat-premium-beef-bone-in-net-weight-50-gm-1-kg").text
    soup=BeautifulSoup(beef_url,'lxml')
    title="Bengal Meat Beef Bone in (Net Weight ± 50 gm) "
    quantity="1kg"
    price_amounts=soup.select(".discountedPrice >span")
    price=price_amounts[1].text
    beef_dict4={}
    beef_dict4['title']=title
    beef_dict4['quantity']=quantity
    beef_dict4['price']=price
    return beef_dict4
    
@app.route('/',methods=['GET','POST'])
def home():
    all_products_list=[]
    
    search_item=request.form.get('product')
    print(search_item)    
    if search_item == 'chicken' or search_item=='boiler chicken' or search_item=='Chicken' or search_item=='desi chicken':
        search_item2="chicken"
        shopno_url=requests.get("https://www.shwapno.com/products/meat--fish-meat-"+search_item2+"/other/broiler-chicken-without-skin-per-kg/pid-12100222.aspx").text
        soup=BeautifulSoup(shopno_url,'lxml')
        
        title="Broiler Chicken Without Skin per Kg"
        quantity="1kg"
        price_amounts=soup.select("#lblOfferPrice >span")
        price=price_amounts[1].text
        
        chicken_dict1={}
        chicken_dict1['title']=title
        chicken_dict1['quantity']=quantity
        chicken_dict1['price']=price
        all_products_list.append(chicken_dict1)
        
        #chicken with skin
        shopno_url2=requests.get("https://www.shwapno.com/products/meat--fish-meat-chicken/other/broiler-chicken-with-skin-per-kg/pid-12100234.aspx").text
        soup=BeautifulSoup(shopno_url2,'lxml')
        title="Broiler Chicken With Skin per Kg"
        quantity="1kg"
        price_amounts=soup.select('.productprices .offer .sp_amt')
        price=price_amounts[0].text
        chicken_dict2={}
        chicken_dict2['title']=title
        chicken_dict2['quantity']=quantity
        chicken_dict2['price']=price
        all_products_list.append(chicken_dict2)
        
        #local chicken
        shopno_url3=requests.get("https://www.shwapno.com/products/meat--fish-meat-chicken/na/local-chicken-dressed-(pcs)/pid-15125889.aspx").text
        soup=BeautifulSoup(shopno_url3,'lxml')
        title=" Local Chicken Dressed (Pcs)"
        quantity="1kg"
        price_amounts=soup.select('.productprices .offer .sp_amt')
        price=price_amounts[0].text
        chicken_dict3={}
        chicken_dict3['title']=title
        chicken_dict3['quantity']=quantity
        chicken_dict3['price']=price
        all_products_list.append(chicken_dict3)
       
        #Shonanika chicken
        shopno_url4=requests.get("https://www.shwapno.com/products/meat--fish-meat-chicken/na/shonalika-chicken-without-skin-(pcs)/pid-15590271.aspx").text
        soup=BeautifulSoup(shopno_url3,'lxml')
        title=" Shonalika Chicken Without skin (Pcs)"
        quantity="1kg"
        price_amounts=soup.select('.productprices .offer .sp_amt')
        price=price_amounts[0].text
        chicken_dict4={}
        chicken_dict4['title']=title
        chicken_dict4['quantity']=quantity
        chicken_dict4['price']=price
        all_products_list.append(chicken_dict4)
        

        #chaldal chicken
        chaldal_url1=requests.get("https://chaldal.com/broiler-chicken-skin-off-net-weight-50-gm-1-kg").text
        soup=BeautifulSoup(chaldal_url1,'lxml')
        title=" Broiler Chicken Skin Off (Net Weight ± 50 gm)"
        quantity="1kg"
        price_amounts=soup.select('.discountedPrice > span >span')
        price=price_amounts[0].text
        chicken_dict5={}
        chicken_dict5['title']=title
        chicken_dict5['quantity']=quantity
        chicken_dict5['price']=price
        all_products_list.append(chicken_dict5)
        

        chaldal_url2=requests.get("https://chaldal.com/broiler-chicken-skin-on-net-weight-50-gm-1-kg").text
        soup=BeautifulSoup(chaldal_url2,'lxml')
        title=" Broiler Chicken Skin On (Net Weight ± 50 gm)"
        quantity="1kg"
        price_amounts=soup.select('.discountedPrice > span >span')
        price=price_amounts[0].text
        chicken_dict6={}
        chicken_dict6['title']=title
        chicken_dict6['quantity']=quantity
        chicken_dict6['price']=price
        all_products_list.append(chicken_dict6)


        chaldal_url3=requests.get("https://chaldal.com/cock-chicken-skin-off-net-weight-30-gm-500-gm").text

        soup=BeautifulSoup(chaldal_url3,'lxml')
        title=" Cock Chicken Skin Off (Net Weight ± 30 gm))"
        quantity="0.5gm"
        price_amounts=soup.select('.price > span >span')
        price=price_amounts[0].text
        chicken_dict7={}
        chicken_dict7['title']=title
        chicken_dict7['quantity']=quantity
        chicken_dict7['price']=price
        all_products_list.append(chicken_dict7) 
        print(all_products_list)

    elif search_item=="meat" or search_item=="Meat" or search_item=="gorur mangso" or search_item=="cow meat" or search_item=="beef" or search_item=="Beef":
        beef_item=shopno_beef()
        beef_item2=shopno_beef_item2()
        beef_item3=shopno_beef_item3()
        beef_item4=chaldal_beef()
        all_products_list.append(beef_item)
        all_products_list.append(beef_item2)
        all_products_list.append(beef_item3)
        all_products_list.append(beef_item4)
        print(all_products_list)

        
    return render_template('index.html')

app.run(debug=True)     
from flask import  Flask,render_template,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

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
        
    return render_template('index.html')

app.run(debug=True)     
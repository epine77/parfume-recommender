import requests
from bs4 import BeautifulSoup as bs

brands_url = requests.get('https://www.luckyscent.com/brands')
if brands_url.status_code == 200:
    brands_soup = bs(brands_url.text, 'html.parser')
    brands_list = brands_soup.find(class_='brands-container')
    brands = brands_list.find_all('a')
    for brand in brands:
        print(brand['href'])
else:
    print('An error has occurred.')
   
for brand in brands:
    try:
        get_brand=requests.get(brand['href'])
        if brands_url.status_code == 200:
            parfume_soup = bs(get_brand.text, 'html.parser')
            parfume_list = parfume_soup.find(id='search-results-container') 
            parfumes = parfume_list.find_all('a')
            for parfume in parfumes:
                print(parfume['href'])
        else:
            print('An error has occurred.')
    except:
        print('Мяяяя')
        
for parfume in parfumes:
    try:
        get_desc=requests.get(parfume['href'])
        if get_desc.status_code == 200:
            desc_soup = bs(get_desc.text, 'html.parser')
            desc_list = desc_soup.find_all(class_='form-group')
            #print(name_list)
            name = desc_soup.find(class_='col-sm-12')
            brandname = name.find('span', {'itemprop' : 'name'}).find('h1')
            scoop = desc_list[0].find('p')
            notes = desc_list[1].find('p')
            rating = desc_soup.find(class_='glyph-rating')
            print('rating:' + rating['data-rating'])
            print(scoop.text)
            print(notes.text)
            print(name.text)
            #for p in scoop:
             #   print(p.text)
        else:
            print('An error has occurred.')
    except:
        print('Мяяяя')

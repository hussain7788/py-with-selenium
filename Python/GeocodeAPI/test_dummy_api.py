import requests
import json

endpoint = "https://dummyjson.com/products/"

### How to authenticate Rest API . here we use HTTPBasicAuth authentication like username, password
# basic_authentication = requests.get(
#             'https://api.github.com/user', 
#             auth=HTTPBasicAuth('username', 'password')
#         )

### to access headers 
# print(response.headers)

### Access token
# my_headers = {'Authorization' : 'Bearer {access_token}'}
# response = requests.get('http://httpbin.org/headers', headers=my_headers)

def get_products():
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
    # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

    data = response.json()
    d1 = {
            "products":[]
        }
    for product in data['products']:
        dt = {}
        dt['id'] = product['id']
        dt['title'] = product['title']
        dt['price'] = product['price']
        dt['brand'] = product['brand']
        dt['category'] = product['category']
        d1['products'].append(dt)

    ## sending filtered data to json file to read properly
    with open("sample1.json", 'w') as f2:
        json.dump(d1, f2, indent=4)

    ### send complete data to json file
    with open("sample2.json", 'w') as f1:
        json.dump(data, f1, indent=4)

    print("Fetching data Completed..............")
    print("d1::::", d1)

def add_product():
    url = endpoint + "add"
    data = {'id': 100, 'title': 'Samsung Galaxy Mobile Phone', 'description': 'Samsung Galaxy Book S (2020) Laptop With Intel Lakefield Chip, 8GB of RAM Launched', 'price': 1499, 'discountPercentage': 4.15, 'rating': 4.25, 'stock': 50, 'brand': 'Samsung', 'category': 'laptops', 'thumbnail': 'https://i.dummyjson.com/data/products/7/thumbnail.jpg', 
            'images': ['https://i.dummyjson.com/data/products/7/1.jpg', 'https://i.dummyjson.com/data/products/7/2.jpg', 'https://i.dummyjson.com/data/products/7/3.jpg', 'https://i.dummyjson.com/data/products/7/thumbnail.jpg']}
    response = requests.post(url, data=data) 
    print("add product response:::", response)

def delete_product():
    url = endpoint + "1"
    response = requests.delete(url)
    print("delete product response:::", response)

def update_product():
    url = endpoint + "100"
    data = {'id': 100, 'title': 'micromax mobile phone'}
    response = requests.patch(url, data=data)
    print("update product response:::", response)


get_products()
add_product()
update_product()
delete_product()
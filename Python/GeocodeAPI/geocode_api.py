import requests

api_key = "AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw"
address = "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008"
params = {
    "key": api_key,
    "address": address,
    "output_format": "json"
}

url = "https://maps.googleapis.com/maps/api/geocode/" + params['output_format']

response = requests.get(url, params=params).json()

if response['status'] == "OK":
    addr = response['results'][0]['formatted_address']
    geometry = response['results'][0]['geometry']
    lat = geometry['location']['lat']
    lng = geometry['location']['lng']

    json_response = {
        "coordinates": {
            "lat": lat,
            "lng": lng
        },
        "address": addr}
    print(json_response)

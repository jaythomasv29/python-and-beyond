# find env path command ~ pipenv --venv
import requests
import config

print(config.api_key)



# GET /businesses endpoint
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Thai",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
# print(response.text)
businesses = response.json()["businesses"]
# print(businesses)
top_business_names = [{"name": business["name"], "rating": business["rating"]} for business in businesses if business["rating"] > 3 ]
print(top_business_names)


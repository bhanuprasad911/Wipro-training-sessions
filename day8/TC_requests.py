import requests

geturl = "https://api.restful-api.dev/objects"
response = requests.get(geturl)
print("\n")
print("GET RESPONSE")
print("-"*30)
print(response.status_code)
print(response.json())

posturl = "https://api.restful-api.dev/objects"
body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
response = requests.post(posturl, json=body1)
print("\n")
print("POST RESPONSE")
print("-"*30)
print(response.status_code)
print(response.json())

puturl = "https://api.restful-api.dev/objects/ff8081819782e69e019be405bd3d2e83"
body2 = {
    "name":"Apple"
}
print("\n")

print("PATCH RESPONSE")
print("-"*30)
patch_response = requests.patch(puturl, json=body2)
print(response.status_code)
print(response.json())
print("\n")

print("PUT RESPONSE")
print("-"*30)

put_response = requests.put(puturl, json=body2)
print(put_response.status_code)
print(put_response.json())

print("\n")
print("DELETE RESPONSE")
print("-"*30)

delete_response = requests.delete(puturl)
print(delete_response.status_code)
print(delete_response.json())







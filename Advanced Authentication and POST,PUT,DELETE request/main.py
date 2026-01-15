import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
UserName = "andreijohn"
GraphId ="graph1"
TOKEN= "sekuhrfkeuhsbf8qawa23"
NEW_TOKEN = "ajklfhjaksebfkajs2"
pixela_params={
    "token":NEW_TOKEN ,
    "username": UserName,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

#CREATING A USER
# respone = requests.post(pixela_endpoint, json=pixela_params)
# print(respone.text)

graph_endpoint = f"{pixela_endpoint}/{UserName}/graphs"


graph_header = {
    "X-USER-TOKEN": NEW_TOKEN
}
graph_params = {
    "id": GraphId,
    "name": "Code Graph",
    "unit": "hours",
    "type":"float",
    "color":"ajisai"
}

# response = requests.post(graph_endpoint, json=graph_params, headers=graph_header)
# print(response.text)

pixelPost_endpoint = f"{pixela_endpoint}/{UserName}/graphs/{GraphId}"

today = datetime.now()
# today = datetime(year=2026, month=1, day=14)
# print(today.strftime("%Y%m%d"))

#Autofilling todays date using strftime method
PixelPost_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours  did you code today?")
}

response = requests.post(url=pixelPost_endpoint, json=PixelPost_params, headers= graph_header)
print(response.text)

# DELETE - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# delete_endpoint = f"{pixela_endpoint}/{UserName}/graphs/{GraphId}/{20260114}"

# response = requests.delete(delete_endpoint,headers= graph_header)
# print(response.text)




# PUT -/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
Update_endpoint = f"{pixela_endpoint}/{UserName}/graphs/{GraphId}/{20260114}"

Update_params ={
    "quantity":"2.5"
}

# response = requests.put(Update_endpoint, json= Update_params, headers=graph_header)
# print(response.text)
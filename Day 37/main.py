import requests
from datetime import datetime

username = "harshgadhiya"
token = "7g6h98gsfh98onfg76th8osg"
graphid = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphid}"


user_params = {
    "token":token,
    "username": username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_params = {
    "id":"graph2",
    "name":"Reading Graph",
    "unit":"Pages",
    "type":"int",
    "color":"shibafu"
}

headers = {
    "X-USER-TOKEN" : token
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)
today = datetime.now()

pixel_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"51",
}

# response = requests.post(url=pixel_creation_endpoint,json=pixel_params,headers=headers)
# print(response.text)
pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphid}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity":"51",
}

response = requests.delete(url=pixel_update_endpoint,headers=headers)
print(response.text)
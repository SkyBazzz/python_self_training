"""
https://pixe.la/v1/users/oleksandrsky/graphs/run1.html
https://pixe.la/@oleksandrsky
"""

import requests
import datetime
BASE_URL = "https://pixe.la/v1/"
API_TOKEN = "scnsiiI@&HNNSKANX@*(!XNLL"
USER_NAME = "oleksandrsky"
RUN_GRAPH_ID = "run1"

users = "users"
graphs = "graphs"

# user_params = {
#     "token": API_TOKEN,
#     "username": "oleksandrsky",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
#
# }

# response = requests.post(url=f"{BASE_URL}{users}", json=user_params)
# print(response.text)
pixel_params = {
    "date": f"{datetime.datetime.now().strftime('%Y%m%d')}",
    "quantity": "2.5",
    "optionalData": "{ 'How do you feel': 'fine'}",
}

headers = {
    "X-USER-TOKEN": API_TOKEN
}

response = requests.post(url=f"{BASE_URL}{users}/{USER_NAME}/{graphs}/{RUN_GRAPH_ID}", json=pixel_params,
                         headers=headers)
print(response.text)

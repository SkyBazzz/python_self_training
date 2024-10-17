# Upload is not special. Select file path and get it by url, then save binary into a file.
# Using files automatically converts into multipart/form-data
# lets upload


import requests

URL = "https://cgi-lib.berkeley.edu/ex/fup.cgi"

with open("input/calendar.txt", mode="rb") as file:
    # 'upfile' it's a name of the field, similar logic for any keys
    resp = requests.post(URL, files={"upfile": file, "note": "mega cool note"}, timeout=10)

print(resp.text)

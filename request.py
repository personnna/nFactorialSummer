import requests

url = "https://file.notion.so/f/s/fbbe6c40-a3f2-4a58-a90b-d8004f62fdcc/names.txt?id=18b71f91-b725-42c4-8d4c-5bf352a5719d&table=block&spaceId=7c849ae7-f9f9-4efe-9968-3fab523bf9e5&expirationTimestamp=1685354680170&signature=Lq1_-EET4PjIm414xjSm4XxLt89rsOQD2dTX_jzqSh4&downloadName=names.txt"

def fetch_names(url):
    response = requests.get(url)
    if response.status_code == 200:
        names_list = response._content.decode('utf-8').split('\n')
        names_list.pop()
        return names_list
    else:
        print("Error: Failed to fetch data. Status code:", response.status_code)
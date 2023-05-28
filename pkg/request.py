import requests

def fetch_names(url):
    response = requests.get(url)
    if response.status_code == 200:
        names_list = response._content.decode('utf-8').split('\n')
        names_list.pop()
        return names_list
    else:
        print("Error: Failed to fetch data. Status code:", response.status_code)
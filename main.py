import requests

url = "https://online-filmek.me"

response = requests.get(url)

if response.status_code == 200:

    content = response.content
    print(content)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)

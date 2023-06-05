import requests
import json

url = "https://filmezek.com/"

def main():
    filmnev = input("").strip()
    response = request_films(filmnev)
    
    if response.status_code != 200:
        print(response.status_code, " HIBA")

    content = json.loads(response.text)

    list_films(content)
        

def list_films(json_content):
    for item in json_content:
        print(item["MovieTitle"])

def request_films(filmnev):
    request_url = url+"searchinput.php?searchType=1&term="+filmnev

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(request_url, headers=headers)
    
    return response

if __name__ == "__main__":
    main()